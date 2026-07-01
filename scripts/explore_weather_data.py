import pandas as pd
from pathlib import Path

# Define project path
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# Define raw file path
rainfall_file = RAW_DATA_DIR / "rainfall_raw.csv"
temperature_file = RAW_DATA_DIR / "temperature_raw.csv"

# Read raw CSV file
rainfall_df = pd.read_csv(rainfall_file)
temperature_df = pd.read_csv(temperature_file)

print("-" * 60)
print("RAINFALL DATA EXPLORATION")
print("-" * 60)

# Basic info
print("\n1. Data Shape:")
print(f" Rows: {rainfall_df.shape[0]}")
print(f" Columns: {rainfall_df.shape[1]}")

# Data Types
print("\n2. Data Types:")
print(rainfall_df.dtypes)

# Missing Values
print("\n3. Missing Values:")
print(rainfall_df.isnull().sum())

# Duplicate Months
print("\n4. Duplicate Months:")
duplicates = rainfall_df["month"].duplicated().sum()
print(f" Number of duplicate months: {duplicates}")

# Date Range
print("\n5. Date Range:")
print(f" First year/month: {rainfall_df['month'].min()}")
print(f" Last year/month: {rainfall_df['month'].max()}")

# Basic Statistic
print("\n6. Basic Statistics:")
print(rainfall_df["total_rainfall"].describe())

# Check negative or zero values
print("\n7. Data Quality Check:")
negative_rainfall = (rainfall_df['total_rainfall'] < 0).sum()
zero_rainfall = (rainfall_df['total_rainfall'] == 0).sum()
print(f" Negative rainfall values: {negative_rainfall}")
print(f" Zero rainfall values: {zero_rainfall}")

print("\n" + "-" * 60)
print("TEMPERATURE DATA EXPLORATION")
print("-" * 60)

# Basic info
print("\n1. Basic Info:")
print(f" Rows: {temperature_df.shape[0]}")
print(f" Columns: {temperature_df.shape[1]}")

# Data types
print("\n2. Data Types:")
print(temperature_df.dtypes)

# Missing values
print("\3. Missing Values:")
print(f" Missing Values: {temperature_df.isnull().sum()}")

# Dupliate months
print("\n4. Duplicate Months:")
duplicates = temperature_df.duplicated().sum()
print(f" Duplicate Months: {duplicates}")

# Date range
print("\n5. Date Range:")
print(f" First Year/Month: {temperature_df["month"].min()}")
print(f" Last Year/Month: {temperature_df["month"].max()}")

# Basic statistics
print("\n6. Basic Statistics:")
print(temperature_df["mean_temp"].describe())

# Check unrealistic values
print("\n7. Data Quality Check:")
temp_below_20 = (temperature_df["mean_temp"] < 20).sum()
temp_above_35 = (temperature_df["mean_temp"] > 35).sum()
print(f" Temperature Below 20°c: {temp_below_20}")
print(f" Temperature Above 35°c: {temp_above_35}")

print("\n" + "-" * 60)
print("EXPLORATION DATA COMPLETE")
print("-" * 60)
