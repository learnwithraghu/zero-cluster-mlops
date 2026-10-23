# Lesson 3 – Train with SageMaker Autopilot

**You will:** train a binary classifier from the S3 training file and create a SageMaker model for batch inference.

1. Open **Amazon SageMaker AI** in the course Region. Go to **AutoML** (or **Autopilot**) and create an AutoML job.
2. Set the input data location to `s3://YOUR_BUCKET/adult-income/train.csv`. Choose **CSV**, enable the header row, and set the target column to `income`.
3. Choose **Binary classification** if prompted, select your SageMaker execution role, and start the job. Keep the default candidate generation settings for this exercise.
4. When the job completes, review the best candidate's metrics and deploy or create a SageMaker model from that candidate. Choose a memorable model name such as `income-autopilot-model`. An endpoint is not needed for Batch Transform.
5. Record the exact SageMaker model name and confirm its Region. Ensure the model's execution role can read the inference object and write to your S3 output prefix.

Console labels vary between SageMaker Studio versions. If the Studio experience only offers endpoint deployment for a candidate, use the candidate's **Create model** action in Studio before continuing; do not leave a real-time endpoint running.

## Checkpoint

The trained candidate is complete and a SageMaker model resource exists in the same Region as your S3 data.
