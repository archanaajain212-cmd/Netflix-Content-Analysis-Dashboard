import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Find the project folder
project_folder = Path(
    "C:\\Netflix Content Analysis Dashboard\\Data Cleaning and Preparation\\netflix_titles2.csv"
).resolve().parent.parent

# Find the CSV dataset
csv_files = list((project_folder / "Dataset").glob("*.csv"))

if not csv_files:
    print("Error: No CSV file found in the Dataset folder.")

else:
    # Load the dataset
    df = pd.read_csv(csv_files[0])

    print("Dataset loaded successfully!")
    print("Total rows:", df.shape[0])
    print("Total columns:", df.shape[1])

    print("\nFirst 5 rows:")
    print(df.head())

    
# Create the Charts folder
charts_folder = project_folder / "Python_EDA" / "Charts"
charts_folder.mkdir(parents=True, exist_ok=True)

# Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# ==========================================
# Chart 1: Movies vs TV Shows
# ==========================================

content_type = df["type"].value_counts()

content_type.plot(kind="bar", figsize=(10, 6))

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    charts_folder / "01_content_type.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Chart 2: Top 10 Countries by Content
# ==========================================

countries = (
    df["country"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

countries = countries[
    countries.ne("")
    & countries.str.lower().ne("unknown")
]

top_countries = countries.value_counts().head(10)

top_countries.plot(kind="bar", figsize=(12, 6))

plt.title("Top 10 Countries by Netflix Titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    charts_folder / "02_top_10_countries.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Chart 3: Content by Release Year
# ==========================================

yearly_content = (
    df.groupby("release_year")["title"]
    .count()
    .sort_index()
)

yearly_content.plot(
    kind="line",
    figsize=(12, 6),
    marker="o"
)

plt.title("Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    charts_folder / "03_release_year_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Chart 4: Top 10 Genres
# ==========================================

genres = (
    df["listed_in"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

top_genres = genres.value_counts().head(10)

top_genres.plot(kind="bar", figsize=(12, 6))

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    charts_folder / "04_top_10_genres.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Chart 5: Content Ratings
# ==========================================

ratings = (
    df["rating"]
    .fillna("Unknown")
    .value_counts()
    .head(10)
)

ratings.plot(kind="bar", figsize=(12, 6))

plt.title("Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    charts_folder / "05_content_ratings.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Chart 6: Movie Duration Distribution
# ==========================================

movies = df[df["type"] == "Movie"].copy()

movies["duration_minutes"] = pd.to_numeric(
    movies["duration"]
    .str.extract(r"(\d+)")[0],
    errors="coerce"
)

movie_duration = movies["duration_minutes"].dropna()

movie_duration.plot(
    kind="hist",
    bins=20,
    figsize=(12, 6)
)

plt.title("Distribution of Movie Durations")
plt.xlabel("Duration in Minutes")
plt.ylabel("Number of Movies")
plt.tight_layout()

plt.savefig(
    charts_folder / "06_movie_duration.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Chart 7: Netflix Content Added by Year
# ==========================================

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

added_year = (
    df["date_added"]
    .dropna()
    .dt.year
    .value_counts()
    .sort_index()
)

added_year.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Netflix Content Added by Year")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    charts_folder / "07_content_added_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Chart 8: Movies vs TV Shows by Release Year
# ==========================================

content_by_year = pd.crosstab(
    df["release_year"],
    df["type"]
)

content_by_year.tail(20).plot(
    kind="bar",
    figsize=(14, 7)
)

plt.title("Movies vs TV Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    charts_folder / "08_content_by_release_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Correlation Analysis
# ==========================================

movies = df[df["type"] == "Movie"].copy()

movies["duration_minutes"] = pd.to_numeric(
    movies["duration"]
    .str.extract(r"(\d+)")[0],
    errors="coerce"
)

correlation = movies[
    ["release_year", "duration_minutes"]
].corr()

print("\nCorrelation Analysis:")
print(correlation)

plt.figure(figsize=(8, 6))

plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        value = correlation.iloc[i, j]
        plt.text(j, i, f"{value:.2f}", ha="center", va="center")

plt.title("Correlation: Release Year vs Movie Duration")
plt.tight_layout()

plt.savefig(
    charts_folder / "09_correlation_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# Python EDA Summary Report
# ==========================================

report_path = (
    project_folder
    / "Python_EDA"
    / "python_eda_summary.txt"
)

report_path.parent.mkdir(parents=True, exist_ok=True)

with open(report_path, "w", encoding="utf-8") as file:

    file.write("NETFLIX CONTENT ANALYSIS\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total Records: {df.shape[0]}\n")
    file.write(f"Total Columns: {df.shape[1]}\n\n")

    file.write("Column Names:\n")
    file.write(", ".join(df.columns) + "\n\n")

    file.write("Missing Values:\n")
    file.write(df.isnull().sum().to_string())
    file.write("\n\n")

    file.write(
        f"Duplicate Rows: {df.duplicated().sum()}\n\n"
    )

    file.write("Data Types:\n")
    file.write(df.dtypes.to_string())
    file.write("\n\n")

    file.write("Summary Statistics:\n")
    file.write(df.describe(include="all").to_string())
    file.write("\n\n")

    file.write("Top 10 Countries:\n")
    file.write(top_countries.to_string())
    file.write("\n\n")

    file.write("Top 10 Genres:\n")
    file.write(top_genres.to_string())
    file.write("\n\n")

    file.write("Content Type Distribution:\n")
    file.write(content_type.to_string())
    file.write("\n\n")

    file.write("Correlation Analysis:\n")
    file.write(correlation.to_string())
    file.write("\n")

print("\nPython EDA completed successfully!")
print("Charts saved in:", charts_folder)
print("Summary report saved at:", report_path)