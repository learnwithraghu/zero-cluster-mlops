# Lesson 1 – Set Up AWS

**You will:** create an S3 bucket and the IAM roles used by SageMaker and ECS.

1. In the AWS Management Console, select the Region for the course.
2. Open **Amazon S3** and create a globally unique bucket, for example `zero-cluster-mlops-<account-id>-<region>`. Keep Block Public Access enabled and use the default encryption.
3. Open **IAM → Roles → Create role**. Create a SageMaker execution role trusted by **SageMaker**. Attach `AmazonSageMakerFullAccess` for this learning project and add an inline S3 policy scoped to your course bucket for reading inputs and writing model artifacts and transform output.
4. Create an ECS task role trusted by **Elastic Container Service Task**. Give it permission to create and describe SageMaker transform jobs, write metrics to CloudWatch, and read/write the course bucket. Use the least privilege you can; for a learning account, `AmazonSageMakerFullAccess` plus a bucket-scoped S3 policy is a simple starting point.
5. Create an ECS task execution role trusted by **Elastic Container Service Task** and attach `AmazonECSTaskExecutionRolePolicy`. ECS uses this role to pull the image and send container logs.
6. In **CloudWatch → Logs**, create a log group named `/zero-cluster-mlops/aws-batch-job`.

Never store access keys in the container or repository. ECS supplies temporary credentials through the task role.

## Checkpoint

The bucket, SageMaker execution role, ECS task role, task execution role, and CloudWatch log group exist in the selected Region.
