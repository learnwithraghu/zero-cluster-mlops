# Zero Cluster MLOps on AWS

Build a serverless binary-classification workflow using SageMaker Autopilot for training, SageMaker Batch Transform for inference, and an ECS Fargate task for orchestration. EventBridge schedules the task, while CloudWatch and X-Ray provide observability.

Start with [Lesson 0: Overview](lessons/00-overview.md). The batch-scoring container is in [`job/`](job/); prepare the Adult Census data with [`data/prepare_adult.py`](data/prepare_adult.py).

## Lessons

1. [Overview and architecture](lessons/00-overview.md)
2. [Set up AWS](lessons/01-project-setup.md)
3. [Prepare and upload data](lessons/02-prepare-data.md)
4. [Train a model with SageMaker Autopilot](lessons/03-train-model.md)
5. [Run Batch Transform](lessons/04-batch-transform.md)
6. [Deploy the Fargate scoring task](lessons/05-fargate-job.md)
7. [Schedule and observe jobs](lessons/06-schedule-observability.md)
8. [Cost control and cleanup](lessons/07-monitoring-cleanup.md)

The AWS Console is used for setup and model training. Python is used once to prepare the public dataset and in the scoring container.
