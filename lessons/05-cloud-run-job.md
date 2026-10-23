# Lesson 5 – Cloud Run Job for Batch Scoring

**You will:** deploy `/job` from your GitHub repo as a Cloud Run Job and run it from the console.

## Prerequisite
Fork or push this repository to your own GitHub account so the console can access it (`job/` contains `main.py`, `Dockerfile`, `requirements.txt`).

## Steps
1. ☰ → **Cloud Run** → **Jobs** tab → **Deploy container** (or **Create job**).
2. Choose **Continuously deploy from a repository (source or function)** → **Set up with Cloud Build**.
3. Authenticate with GitHub, pick your repository and branch, then click **Next**.
4. Build type: **Dockerfile**, **Source location**: `/job/Dockerfile`. Click **Save**.
5. Job settings:
   - **Job name:** `batch-scoring`
   - **Region:** `us-central1` (any region works; BigQuery location is US)
   - Expand **Container, Volumes, Connections, Security**:
     - **Variables & Secrets** → add `PROJECT_ID` = your project ID, `BQ_DATASET` = `mlops_demo`, `BQ_MODEL` = `income_model`
     - **Security** → Service account: `mlops-job-sa`
     - **Task timeout** 600s, **Retries** 1, **Tasks** 1
6. Click **Create**. Cloud Build builds the image first (watch under **Cloud Build → History**); the job appears when finished.
7. Open the job → **Execute**. Under **Executions** open the run and check the **Logs** tab for `Scored N rows`.
8. In BigQuery Studio confirm the table `mlops_demo.predictions` exists.

## Troubleshooting
- *Permission denied on BigQuery*: re-check roles of `mlops-job-sa` (Lesson 1).
- *Build failed*: **Cloud Build → History** shows logs; ensure Dockerfile path is `/job/Dockerfile`.
- *Model not found*: model and dataset must be in the same `US` location.

## Checkpoint
A successful execution (green tick) and a populated `predictions` table.
