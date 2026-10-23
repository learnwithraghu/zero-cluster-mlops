# Lesson 2 – Explore Public Data in BigQuery

**You will:** open a Google public dataset and create your own dataset for the model.

## Steps
1. ☰ → **BigQuery** → **BigQuery Studio**.
2. In the **Explorer** panel click **+ Add** → **Star a project by name** → enter `bigquery-public-data` → **Star**.
3. Expand `bigquery-public-data` → `ml_datasets` → `census_adult_income`. Open the **Schema** and **Preview** tabs. Columns include `age`, `workclass`, `education_num`, `occupation`, `hours_per_week`, and the label `income_bracket`.
4. Create your dataset: next to your project in Explorer click **⋮** → **Create dataset**.
   - Dataset ID: `mlops_demo`
   - Location type: **Multi-region → US** (must match the public data location, which is US).
   - Click **Create dataset**.
5. Click **SQL query** (new editor tab) and run:
   ```sql
   SELECT income_bracket, COUNT(*) AS n, AVG(age) AS avg_age
   FROM `bigquery-public-data.ml_datasets.census_adult_income`
   GROUP BY income_bracket;
   ```
6. Check the query validator (green tick, top-right of the editor) shows bytes processed – this is how you estimate cost.

## Checkpoint
You see two income brackets and your `mlops_demo` dataset exists in `US`.
