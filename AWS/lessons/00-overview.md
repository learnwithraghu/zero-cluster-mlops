# Lesson 0 – Overview, Architecture and Prerequisites

**Goal:** build a scheduled, serverless batch-ML workflow without managing a cluster.

## Architecture

| Concern | AWS service |
|---|---|
| Data storage | Amazon S3 |
| Model training | SageMaker Autopilot |
| Batch inference | SageMaker Batch Transform |
| Orchestration | ECS Fargate |
| Scheduling | Amazon EventBridge Scheduler |
| Metrics and logs | Amazon CloudWatch |
| Traces | AWS X-Ray |

```text
UCI Adult Census data ─► S3 ─► SageMaker Autopilot ─► SageMaker model
       │                                                 │
       └──────────────► S3 inference.csv ─► Batch Transform ─► S3 predictions
                                                    ▲
EventBridge Scheduler ─► ECS Fargate task ──────────┘
                                  └─ CloudWatch metrics/logs + X-Ray traces
```

The workflow predicts whether a person's income is above $50K using the public UCI Adult Census dataset.

## Prerequisites

- An AWS account with billing enabled and permission to create IAM roles, S3 buckets, SageMaker resources, ECS tasks, EventBridge schedules, and CloudWatch resources.
- A local Python 3 installation to prepare the public data in Lesson 2.
- Choose one AWS Region and use it for all resources. SageMaker, S3, and ECS resources must be in compatible Regions.

## Checkpoint

You understand the service boundaries and have selected a Region before creating resources.
