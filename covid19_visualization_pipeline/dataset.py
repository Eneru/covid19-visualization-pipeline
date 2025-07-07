import pandas as pd

from covid19_visualization_pipeline.config import (
    COUNTRIES,
    PROCESSED_DATA_PATH,
    PROCESSED_DIR,
    RAW_DIR,
)


def load_data():
    df = pd.read_csv(RAW_DIR / "compact.csv")
    return df


def transform(df):
    df = df[df["country"].isin(COUNTRIES)]
    df = df[["country", "date", "total_cases", "new_cases", "population"]]
    df["date"] = pd.to_datetime(df["date"])
    df["new_cases_per_100k"] = (df["new_cases"] / df["population"]) * 100000
    df["new_cases_7day_avg"] = df.groupby("country")["new_cases"].transform(
        lambda x: x.rolling(7).mean()
    )
    return df.dropna()


def save_data(df):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)


def main():
    print("Loading data...")
    df = load_data()
    print("Transforming data...")
    df_clean = transform(df)
    print("Saving transformed data...")
    save_data(df_clean)
    print("Done.")


if __name__ == "__main__":
    main()
