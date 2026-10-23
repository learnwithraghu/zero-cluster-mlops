"""Submit a SageMaker Batch Transform job and publish CloudWatch metrics."""
import os
import time
import uuid

import boto3
from aws_xray_sdk.core import patch_all, xray_recorder

patch_all()

REGION = os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION")
MODEL_NAME = os.environ["SAGEMAKER_MODEL_NAME"]
INPUT_URI = os.environ["S3_INPUT_URI"]
OUTPUT_PREFIX = os.environ["S3_OUTPUT_PREFIX"].rstrip("/") + "/"
NAMESPACE = os.environ.get("CLOUDWATCH_NAMESPACE", "ZeroClusterMLOps")
INSTANCE_TYPE = os.environ.get("TRANSFORM_INSTANCE_TYPE", "ml.m5.large")
POLL_SECONDS = int(os.environ.get("POLL_SECONDS", "15"))

if not REGION:
    raise RuntimeError("Set AWS_REGION or AWS_DEFAULT_REGION.")

sagemaker = boto3.client("sagemaker", region_name=REGION)
cloudwatch = boto3.client("cloudwatch", region_name=REGION)


def wait_for_transform(job_name):
    while True:
        response = sagemaker.describe_transform_job(TransformJobName=job_name)
        status = response["TransformJobStatus"]
        if status == "Completed":
            return
        if status in {"Failed", "Stopped"}:
            raise RuntimeError(
                f"Transform job {job_name} ended with status {status}: "
                f"{response.get('FailureReason', 'no failure reason provided')}"
            )
        time.sleep(POLL_SECONDS)


def main():
    job_name = f"zero-cluster-{uuid.uuid4().hex[:12]}"
    output_path = f"{OUTPUT_PREFIX}{job_name}/"
    start = time.monotonic()
    xray_recorder.begin_segment("aws_batch_scoring")
    try:
        with xray_recorder.begin_subsegment("create_transform_job"):
            sagemaker.create_transform_job(
                TransformJobName=job_name,
                ModelName=MODEL_NAME,
                TransformInput={
                    "DataSource": {
                        "S3DataSource": {
                            "S3DataType": "S3Prefix",
                            "S3Uri": INPUT_URI,
                        }
                    },
                    "ContentType": "text/csv",
                    "SplitType": "Line",
                },
                TransformOutput={
                    "S3OutputPath": output_path,
                    "Accept": "text/csv",
                    "AssembleWith": "Line",
                },
                TransformResources={
                    "InstanceType": INSTANCE_TYPE,
                    "InstanceCount": 1,
                },
            )
        print(f"Started SageMaker transform job {job_name}")
        with xray_recorder.begin_subsegment("wait_for_transform_job"):
            wait_for_transform(job_name)

        duration = time.monotonic() - start
        cloudwatch.put_metric_data(
            Namespace=NAMESPACE,
            MetricData=[
                {
                    "MetricName": "BatchTransformJobs",
                    "Value": 1,
                    "Unit": "Count",
                    "Dimensions": [{"Name": "ModelName", "Value": MODEL_NAME}],
                },
                {
                    "MetricName": "BatchTransformDurationSeconds",
                    "Value": duration,
                    "Unit": "Seconds",
                    "Dimensions": [{"Name": "ModelName", "Value": MODEL_NAME}],
                },
            ],
        )
        print(f"Transform job {job_name} completed in {duration:.1f}s")
    finally:
        xray_recorder.end_segment()


if __name__ == "__main__":
    main()
