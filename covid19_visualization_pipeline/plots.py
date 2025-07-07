import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

from covid19_visualization_pipeline.config import PLOTS_DIR, PROCESSED_DATA_PATH

PLOTS_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    df = pd.read_csv(PROCESSED_DATA_PATH, parse_dates=["date"])
    return df


def plot_matplotlib_7day_avg(df):
    plt.figure(figsize=(12, 6))
    for country in df["country"].unique():
        subset = df[df["country"] == country]
        plt.plot(subset["date"], subset["new_cases_7day_avg"], label=country)
    plt.title("7-Day Average of New COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("New Cases (7-day avg)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save as PNG and PDF
    plt.savefig(PLOTS_DIR / "fig_cases_avg7.png")
    plt.close()


def plot_plotly_per_100k(df):
    fig = px.line(
        df,
        x="date",
        y="new_cases_per_100k",
        color="country",
        title="New COVID-19 Cases per 100k People",
        labels={"new_cases_per_100k": "Cases per 100k", "date": "Date"},
    )
    fig.write_html(PLOTS_DIR / "fig_cases_per_100k.html")
    # Optional: Save static image (requires kaleido)
    try:
        fig.write_image(PLOTS_DIR / "fig_cases_per_100k.png")
    except ValueError:
        print("⚠️ Skipping PNG save: 'kaleido' not installed. Install with: pip install -U kaleido")


def main():
    df = load_data()
    print("Generating and saving plots...")
    plot_matplotlib_7day_avg(df)
    plot_plotly_per_100k(df)
    print("✅ All plots saved in:", PLOTS_DIR)


if __name__ == "__main__":
    main()
