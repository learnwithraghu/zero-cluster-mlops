# Lesson 5 – Run Batch Scoring from ECS Fargate

**You will:** build the repository's container and run it as an ECS task.

1. Push or fork this repository so your build environment can access it. Build the image from `AWS/job/Dockerfile` with `AWS/job` as the build context, then push it to **Amazon ECR**. The ECR repository must be in the course Region.
2. In **Amazon ECS**, create a Fargate cluster if needed. Create a task definition using the image, the task execution role and task role from Lesson 1, and `awsvpc` networking.
3. Configure container environment variables:
   - `AWS_REGION`: the course Region
   - `SAGEMAKER_MODEL_NAME`: the model from Lesson 3
   - `S3_INPUT_URI`: the inference CSV URI from Lesson 2
   - `S3_OUTPUT_PREFIX`: `s3://YOUR_BUCKET/predictions/automated/`
   - `CLOUDWATCH_NAMESPACE`: `ZeroClusterMLOps`
4. Send container logs to `/zero-cluster-mlops/aws-batch-job`. Configure a security group and subnets with outbound access to AWS APIs (for example, public subnets with auto-assigned public IP, or private subnets with suitable VPC endpoints/NAT).
5. Run a task using Fargate. Open the task's **Logs** tab and wait for the transform job to finish.
6. Verify the task exits successfully and the output prefix contains a SageMaker transform result.

The task role needs permission for `sagemaker:CreateTransformJob`, `sagemaker:DescribeTransformJob`, `s3:GetObject`, `s3:PutObject`, and `cloudwatch:PutMetricData`. The SageMaker model execution role also needs S3 access to the input and output prefixes.

## Checkpoint

The Fargate task has exited successfully, its logs show a completed transform job, and the output exists in S3.
