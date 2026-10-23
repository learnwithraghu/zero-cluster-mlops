# Lesson 3 – Train a Model with BigQuery ML

**You will:** train a logistic regression model using only SQL.

## Steps
1. In BigQuery Studio open a new **SQL query** tab. Make sure the project is yours.
2. Paste and click **Run**. The hash-based filter holds out ~10% of rows (bucket 9) for prediction/evaluation:
   ```sql
   CREATE OR REPLACE MODEL `mlops_demo.income_model`
   OPTIONS (
     model_type = 'LOGISTIC_REG',
     input_label_cols = ['income_bracket'],
     auto_class_weights = TRUE
   ) AS
   SELECT * EXCEPT (functional_weight)
   FROM `bigquery-public-data.ml_datasets.census_adult_income`
   WHERE MOD(ABS(FARM_FINGERPRINT(CAST(functional_weight AS STRING))), 10) < 9;
   ```
   > If your project is not the default one, prefix with `YOUR_PROJECT_ID.`.
3. Wait ~1–2 minutes. In **Explorer** expand `mlops_demo` → **Models** → `income_model`.
4. Browse tabs: **Details**, **Training** (loss curve), **Evaluation**, **Schema**.

## Try it
Change `model_type` to `'BOOSTED_TREE_CLASSIFIER'` and save as `income_model_bt` to compare later.

## Checkpoint
`income_model` appears under Models in `mlops_demo`.
