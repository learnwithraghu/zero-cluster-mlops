# Lesson 1 – Project Setup and Enabling APIs

**You will:** create a project, enable APIs, grant the job's service account permissions.

## Steps
1. Open https://console.cloud.google.com and sign in.
2. Click the **project picker** (top bar, next to the Google Cloud logo) → **New project**.
3. Name it `zero-cluster-mlops`, choose organization/location (or "No organization"), click **Create**. Select it in the project picker once created.
4. Confirm billing: navigation menu (☰) → **Billing** → make sure the project is linked to a billing account.
5. Enable APIs: ☰ → **APIs & Services** → **Library**. Search and click **Enable** for each:
   - BigQuery API (usually already on)
   - Cloud Run Admin API
   - Cloud Build API
   - Artifact Registry API
   - Cloud Scheduler API
   - Cloud Trace API
   - Cloud Monitoring API
   - Cloud Logging API
6. Create a service account for the job: ☰ → **IAM & Admin** → **Service Accounts** → **Create service account**.
   - Name: `mlops-job-sa` → **Create and continue**.
   - Grant roles: `BigQuery Job User`, `BigQuery Data Editor`, `Cloud Trace Agent`, `Monitoring Metric Writer`, `Logs Writer`.
   - Click **Done**.
7. Create another service account `scheduler-sa` with role **Cloud Run Invoker** (used in Lesson 7).

## Checkpoint
IAM & Admin → **IAM** lists your project with both service accounts. APIs & Services → **Enabled APIs** shows the APIs above.
