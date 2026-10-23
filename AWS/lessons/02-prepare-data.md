# Lesson 2 – Prepare and Upload the Public Data

**You will:** turn the UCI Adult Census files into a training CSV and a feature-only batch-inference CSV.

1. Download the two source files from the UCI repository by running the preparation script from the repository root:
   ```sh
   python AWS/data/prepare_adult.py
   ```
   It writes `AWS/data/output/train.csv` and `AWS/data/output/inference.csv`. The training CSV has a header and income label; the inference CSV contains only feature columns.
2. In **Amazon S3**, open your course bucket and create a prefix named `adult-income/`.
3. Upload `train.csv` and `inference.csv` to that prefix. Keep them private.
4. Copy and record both S3 object URIs. You will use the training URI in Lesson 3 and the inference URI in Lesson 4.

The script combines the public `adult.data` and `adult.test` records and normalizes whitespace and the test-file label punctuation. Do not upload any personal data.

## Checkpoint

Both CSV objects are visible under `s3://YOUR_BUCKET/adult-income/`.
