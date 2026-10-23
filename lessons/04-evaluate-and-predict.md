# Lesson 4 – Evaluate and Predict

**You will:** evaluate on held-out data and run predictions.

## Evaluate
```sql
SELECT * FROM ML.EVALUATE(MODEL `mlops_demo.income_model`, (
  SELECT * EXCEPT (functional_weight)
  FROM `bigquery-public-data.ml_datasets.census_adult_income`
  WHERE MOD(ABS(FARM_FINGERPRINT(CAST(functional_weight AS STRING))), 10) = 9));
```
Look at `precision`, `recall`, `accuracy`, `f1_score`, `roc_auc`.

## Predict
```sql
SELECT predicted_income_bracket, predicted_income_bracket_probs, age, occupation
FROM ML.PREDICT(MODEL `mlops_demo.income_model`, (
  SELECT * FROM `bigquery-public-data.ml_datasets.census_adult_income` LIMIT 20));
```

## Explain (optional)
```sql
SELECT * FROM ML.GLOBAL_EXPLAIN(MODEL `mlops_demo.income_model`);
```

## Save a result via the console
Run the evaluate query → **Save results** → **BigQuery table** → dataset `mlops_demo`, table `eval_baseline`.

## Checkpoint
You have metrics and predictions. These queries are what the Cloud Run Job automates next.
