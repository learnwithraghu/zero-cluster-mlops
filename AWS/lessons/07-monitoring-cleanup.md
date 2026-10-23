# Lesson 7 – Cost Control and Cleanup

## Cost control

- SageMaker Autopilot and Batch Transform can incur compute charges. Stop or delete resources when they are not in use.
- ECS Fargate charges for task runtime; avoid leaving services running for this batch workflow.
- S3 storage and CloudWatch logs/metrics also incur charges. Set a CloudWatch budget alert in **Billing and Cost Management → Budgets**.
- Delete any SageMaker real-time endpoint created during experimentation; Batch Transform does not need one.

## Cleanup

Delete resources in this order:

1. Delete the EventBridge schedule.
2. Stop any running ECS tasks, then delete the ECS task definition revisions and cluster if created just for this course.
3. Delete SageMaker transform jobs and the SageMaker model. Delete the Autopilot job and model artifacts when no longer needed.
4. Delete the course S3 bucket contents and bucket.
5. Delete the CloudWatch log group and custom metrics after their retention period.
6. Delete IAM roles created only for this course after confirming no other resources use them.
7. Delete the ECR image and repository.

## Congratulations

You trained a model, ran batch inference, and scheduled a serverless pipeline on AWS without managing a cluster.
