# Lesson 7 – Schedule and Automate

**You will:** run the job daily, and retrain the model on a schedule.

## Schedule the Cloud Run Job
1. Open Cloud Run → **Jobs** → `batch-scoring` → **Triggers** tab → **Add Scheduler Trigger**.
2. Name `daily-batch-scoring`, Frequency `0 6 * * *`, Timezone of your choice.
3. Service account: `scheduler-sa` (role *Cloud Run Invoker*). Click **Create**.
4. Verify in ☰ → **Cloud Scheduler** → select the schedule → **Force run**, then confirm a new execution on the job.

## Scheduled retraining with BigQuery
1. BigQuery Studio → paste the `CREATE OR REPLACE MODEL` query from Lesson 3 → **Schedule** → **Create new scheduled query**.
2. Name `retrain-income-model`, repeats **Daily/Weekly**, start time before the scoring job (e.g. 05:00).
3. Choose the location US and save. Approve the authorization prompt.
4. Check runs under BigQuery → **Scheduled queries**.

## Checkpoint
Both schedules exist; forcing a run produces a new job execution.
