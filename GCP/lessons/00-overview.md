# Lesson 0 – Overview, Architecture and Prerequisites

**Goal:** understand the "zero-cluster" MLOps pattern before building it.

## The idea
Classic MLOps needs Kubernetes, Kubeflow or Airflow clusters. This course uses only serverless pieces:

| Concern | Service |
|---|---|
| Data + training + inference | **BigQuery ML** (SQL only) over a Google public dataset |
| Batch scoring / orchestration code | **Cloud Run Jobs** |
| Scheduling | **Cloud Scheduler** |
| Observability | **OpenTelemetry** → Cloud Trace + Cloud Monitoring |

```
BigQuery public data ─► BQML CREATE MODEL ─► Cloud Run Job (ML.PREDICT + OTel)
                                                   ▲                  │
                                          Cloud Scheduler             ▼
                                                           Cloud Trace / Monitoring
```

## Dataset
`bigquery-public-data.ml_datasets.census_adult_income` – predict whether income is `>50K` (binary classification). No data upload needed.

## Prerequisites
- A Google account and a GCP project with **billing enabled** (new accounts get free credits).
- A GitHub account (to deploy the job from this repository via the console).
- Only a browser: **everything uses the Google Cloud console (https://console.cloud.google.com)**. No `gcloud`.

> The console UI changes often. If a label differs slightly, use the console search bar (top, or press `/`) to find the page.

## Lessons
1. [Project setup & APIs](01-project-setup.md)
2. [Explore public data](02-explore-public-data.md)
3. [Train a model with BigQuery ML](03-train-model-bqml.md)
4. [Evaluate and predict](04-evaluate-and-predict.md)
5. [Cloud Run Job for batch scoring](05-cloud-run-job.md)
6. [OpenTelemetry observability](06-opentelemetry.md)
7. [Schedule & automate](07-schedule-automation.md)
8. [Monitoring, alerts, cost & cleanup](08-monitoring-and-cleanup.md)

Job source code lives in [`/job`](../job).
