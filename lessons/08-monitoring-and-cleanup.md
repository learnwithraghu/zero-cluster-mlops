# Lesson 8 – Alerts, Cost Control and Cleanup

## Alert on failures
1. ☰ → **Monitoring** → **Alerting** → **Create policy**.
2. **Select a metric** → *Cloud Run Job* → **Job** → `Completed execution count`, filter `result = failed`. Next.
3. Threshold: above `0` for 1 minute. Next.
4. Notification channel: **Manage notification channels** → add Email → select it. Name the policy `batch-scoring-failed` → **Create policy**.

## Alert on custom OTel metric (optional)
Create a second policy on `batch_predictions_rows` with condition *below 1* so you notice empty runs.

## Cost control
- BigQuery on-demand charges per TB scanned; check bytes in the query validator.
- ☰ → **Billing** → **Budgets & alerts** → **Create budget** (e.g. $10, alerts at 50/90%).
- Cloud Run Jobs bill only while executing.

## Cleanup
1. Cloud Scheduler: delete `daily-batch-scoring`.
2. Cloud Run → Jobs: delete `batch-scoring`.
3. BigQuery: delete the `mlops_demo` dataset (tick *delete contents*), cancel the scheduled query.
4. Artifact Registry: delete the `cloud-run-source-deploy` repository.
5. Or simply: ☰ → **IAM & Admin** → **Settings** → **Shut down** the project.

## Congratulations
You built training, batch inference, scheduling and telemetry with no clusters.
