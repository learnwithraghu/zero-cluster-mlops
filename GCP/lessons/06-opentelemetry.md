# Lesson 6 – Observability with OpenTelemetry

**You will:** read the traces and metrics that `job/main.py` already emits.

## How the code works
- `TracerProvider` + `CloudTraceSpanExporter` send spans to **Cloud Trace**. Each BigQuery call is a child span (`predict`, `count`) under `batch_scoring`, tagged with `bq.job_id` and `bq.bytes_processed`.
- `MeterProvider` + `CloudMonitoringMetricsExporter` send custom metrics `batch_predictions_rows` (counter) and `batch_job_duration_seconds` (histogram) to **Cloud Monitoring**.
- `force_flush()` at the end matters: a job container exits quickly and would otherwise lose buffered telemetry.

## Steps
1. Run the job again (Cloud Run → Jobs → `batch-scoring` → **Execute**).
2. **Traces:** ☰ → **Trace** → **Trace explorer**. Filter span name `batch_scoring`. Click a trace and view the waterfall; click the `predict` span to see its attributes.
3. **Metrics:** ☰ → **Monitoring** → **Metrics explorer**. Click **Select a metric**, search `batch_predictions_rows` (under *Workload* / *custom.googleapis.com/opentelemetry*) → **Apply**. Repeat for `batch_job_duration_seconds`.
4. **Logs:** Cloud Run → job execution → **Logs**, or ☰ → **Logging** → **Logs Explorer**.

## Exercise
Add a span attribute (e.g. model name) in `main.py`, commit to GitHub; Cloud Build redeploys automatically; execute and find the attribute in Trace.

## Checkpoint
You can see one trace with two child spans and both custom metrics.
