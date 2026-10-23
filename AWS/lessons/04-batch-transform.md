# Lesson 4 – Run SageMaker Batch Transform

**You will:** run an on-demand transform to verify the model and data before automating it.

1. Open **Amazon SageMaker AI → Inference → Batch transform jobs → Create batch transform job**.
2. Choose the model from Lesson 3. Set a unique job name and a small instance type supported by the model.
3. Set input to `s3://YOUR_BUCKET/adult-income/inference.csv`, content type `text/csv`, and split type **Line**. Set output to a new prefix, for example `s3://YOUR_BUCKET/predictions/manual/`.
4. Leave input compression disabled and output content type as `text/csv`. Start the job and wait for **Completed**.
5. Open the S3 output prefix and inspect the generated part file. SageMaker writes prediction results there; it does not update the input file.

If the transform fails, inspect the job's failure reason. Check that the input has no header, matches the model's feature order, and that the model execution role can access both S3 prefixes.

## Checkpoint

A completed transform job has written output to the predictions prefix in S3.
