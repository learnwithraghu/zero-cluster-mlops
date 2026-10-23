# Lesson 6 – Schedule and Observe the Job

**You will:** schedule the ECS task and inspect its logs, metrics, and traces.

## Schedule

1. Open **Amazon EventBridge → Scheduler → Create schedule**.
2. Choose a daily schedule (for example, `cron(0 6 * * ? *)`) and the course time zone.
3. Set the target to **Amazon ECS → RunTask**, choose the Fargate cluster and task definition, and configure the networking the same way as Lesson 5.
4. Create or select an EventBridge Scheduler execution role that can run the task and pass the ECS task and execution roles. Use **Flexible time window: Off** for predictable lesson runs.
5. Use **Run now** or wait for the next occurrence, then confirm a new task appears in ECS.

## Observe

- **Logs:** CloudWatch → Logs → `/zero-cluster-mlops/aws-batch-job`. The task logs include the SageMaker transform job name and final status.
- **Metrics:** CloudWatch → Metrics → `ZeroClusterMLOps`. The container publishes `BatchTransformJobs` and `BatchTransformDurationSeconds`.
- **Traces:** the container sends AWS SDK subsegments to the X-Ray daemon at `127.0.0.1:2000`. To view traces, add the AWS X-Ray daemon as a sidecar container in the ECS task definition, expose its UDP port 2000 to the task, and give the task role `xray:PutTraceSegments` and `xray:PutTelemetryRecords`. Then open **AWS X-Ray → Traces** and find the `aws_batch_scoring` segment.

The trace sidecar is optional for running the job; metrics and logs work without it.

## Checkpoint

A scheduled ECS task runs successfully, and you can find its logs and custom CloudWatch metrics.
