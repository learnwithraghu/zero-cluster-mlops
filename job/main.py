"""Batch scoring job: runs BigQuery ML predictions and emits OpenTelemetry traces/metrics."""
import os
import time

from google.cloud import bigquery
from opentelemetry import metrics, trace
from opentelemetry.exporter.cloud_monitoring import CloudMonitoringMetricsExporter
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

PROJECT = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ["PROJECT_ID"]
DATASET = os.environ.get("BQ_DATASET", "mlops_demo")
MODEL = os.environ.get("BQ_MODEL", "income_model")

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(CloudTraceSpanExporter(project_id=PROJECT)))
metrics.set_meter_provider(MeterProvider(metric_readers=[
    PeriodicExportingMetricReader(
        CloudMonitoringMetricsExporter(project_id=PROJECT),
        export_interval_millis=5000)]))

tracer = trace.get_tracer("zero-cluster-mlops")
meter = metrics.get_meter("zero-cluster-mlops")
rows_counter = meter.create_counter("batch_predictions_rows", description="Rows scored")
duration_hist = meter.create_histogram("batch_job_duration_seconds", unit="s")


def run_sql(client, name, sql):
    with tracer.start_as_current_span(name) as span:
        job = client.query(sql)
        result = job.result()
        span.set_attribute("bq.job_id", job.job_id)
        span.set_attribute("bq.bytes_processed", job.total_bytes_processed or 0)
        return result


def main():
    start = time.time()
    client = bigquery.Client(project=PROJECT)
    with tracer.start_as_current_span("batch_scoring"):
        run_sql(client, "predict", f"""
            CREATE OR REPLACE TABLE `{PROJECT}.{DATASET}.predictions` AS
            SELECT * FROM ML.PREDICT(MODEL `{PROJECT}.{DATASET}.{MODEL}`,
              (SELECT * FROM `bigquery-public-data.ml_datasets.census_adult_income`
               WHERE MOD(ABS(FARM_FINGERPRINT(CAST(functional_weight AS STRING))), 10) = 9))
        """)
        count = list(run_sql(client, "count",
            f"SELECT COUNT(*) AS n FROM `{PROJECT}.{DATASET}.predictions`"))[0].n
        rows_counter.add(count)
    duration_hist.record(time.time() - start)
    print(f"Scored {count} rows in {time.time() - start:.1f}s")
    metrics.get_meter_provider().force_flush()
    trace.get_tracer_provider().force_flush()


if __name__ == "__main__":
    main()
