import pandas as pd
from pathlib import Path

# Define project path
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESS_DATA_DIR = BASE_DIR / "data" / "processed"

# Ensure processed data folder exists
PROCESS_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Define file path
rainfall_file = RAW_DATA_DIR / "rainfall_raw.csv"
temperature_file = RAW_DATA_DIR / "temperature_raw.csv"

# Read raw CSV file
rainfall_df = pd.read_csv(rainfall_file)
temperature_df = pd.read_csv(temperature_file)

print("-" * 60)
print("TRANSFORMING WEATHER DATA")
print("-" * 60)

# Step 1: Convert month to datetime
print("\nStep 1: Converting month column to datetime...")
rainfall_df["record_month"] = pd.to_datetime(rainfall_df["month"])
temperature_df["record_month"] = pd.to_datetime(temperature_df["month"])
print("Conversion successful.")

# Extract year and month_number
print("\nStep 2: Extracting year and month_number...")
rainfall_df['year'] = rainfall_df["record_month"].dt.year
rainfall_df['month_number'] = rainfall_df["record_month"].dt.month

temperature_df['year'] = temperature_df["record_month"].dt.year
temperature_df['month_number'] = temperature_df["record_month"].dt.month
print("Extraction successful.")

# Rename columns to final clean names
print("\nStep 3: Renaming columns...")
rainfall_df = rainfall_df.rename(
    columns={"total_rainfall": "total_rainfall_mm"})
temperature_df = temperature_df.rename(
    columns={"mean_temp": "mean_temperature_c"})
print("Renaming successful.")

# Select the needed columns
print("\nStep 4: Selecting final columns...")
rainfall_cleaned = rainfall_df[['record_month',
                                'year', 'month_number', 'total_rainfall_mm']]
temperature_cleaned = temperature_df[[
    'record_month', 'year', 'month_number', 'mean_temperature_c']]
print("Columns selected successfully.")

# Merge rainfall and temperature on record_month
print("\nStep 5: Merging rainfall and temperature datasets...")
weather_df = pd.merge(
    rainfall_cleaned,
    temperature_cleaned,
    on=['record_month', 'year', 'month_number'],
    how='inner'
)
print(
    f"Merged dataset has {weather_df.shape} rows, and {weather_df.shape} columns")

# Check merged data
print("\nStep 6: Checking merged dataset...")
print(weather_df.head())
print("Missing values in merge data:")
missing_value = weather_df.isnull().sum()
print(f"Missing values: {missing_value}")

# Save cleaned dataset
print("\nStep 7: Saving cleaned dataset...")
output_file = PROCESS_DATA_DIR / "weather_cleaned.csv"
weather_df.to_csv(output_file, index=False)
print(f"Cleaned data saved to: {output_file}")

print("\n" + "=" * 60)
print("TRANSFORMATION COMPLETE")
print("=" * 60)
