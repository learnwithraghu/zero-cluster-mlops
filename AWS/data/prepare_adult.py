"""Download and prepare the public UCI Adult Census data for the AWS lessons."""
import csv
from pathlib import Path
from urllib.request import urlopen


DATA_DIR = Path(__file__).parent
OUTPUT_DIR = DATA_DIR / "output"
TRAIN_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
TEST_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"
FIELDS = [
    "age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
    "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income",
]


def read_records(url, skip_test_header=False):
    with urlopen(url, timeout=30) as response:
        lines = response.read().decode("utf-8").splitlines()
    if skip_test_header:
        lines = lines[1:]
    for row in csv.reader(lines, skipinitialspace=True):
        if not row:
            continue
        if len(row) != len(FIELDS):
            raise ValueError(f"Unexpected Adult Census row with {len(row)} columns.")
        record = [value.strip() for value in row]
        record[-1] = record[-1].removesuffix(".")
        yield record


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = list(read_records(TRAIN_URL))
    rows.extend(read_records(TEST_URL, skip_test_header=True))
    training_rows = [row for index, row in enumerate(rows) if index % 10 != 0]
    inference_rows = [row[:-1] for index, row in enumerate(rows) if index % 10 == 0]

    with (OUTPUT_DIR / "train.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(FIELDS)
        writer.writerows(training_rows)

    with (OUTPUT_DIR / "inference.csv").open("w", newline="", encoding="utf-8") as stream:
        csv.writer(stream).writerows(inference_rows)
    print(f"Wrote {len(training_rows)} training records and {len(inference_rows)} inference records.")


if __name__ == "__main__":
    main()
