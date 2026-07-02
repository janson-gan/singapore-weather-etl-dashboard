import pandas as pd
from pathlib import Path

# Define the path
BASE_DIR = Path(__file__).parent.parent
PROCESS_DATA_DIR = BASE_DIR / "data" / "processed"

# Define cleaned file
clean_file = PROCESS_DATA_DIR / "weather_cleaned.csv"

# Read cleaned file
weather_cleaned_df = pd.read_csv(clean_file)

print("\n" + "-" * 60)
print("VALIDATING WEATHER CLEANED FILE")
print("-" * 60)

# Check total rows and columns
print("\n1. Check rows and columns:")
print(f"Rows: {weather_cleaned_df.shape[0]}")
print(f"Columns: {weather_cleaned_df.shape[1]}")

# Check missing values
print("\n2. Check missing values:")
print(f"Missing values: {weather_cleaned_df.isnull().sum()}")

# Check duplicates values
print("\n3. Check duplicate values:")
print(f"Duplicate values: {weather_cleaned_df.duplicated().sum()}")

# Check rainfall 
# 7. Rainfall validation
print("\n7. Rainfall Validation:")
negative_rainfall = (weather_cleaned_df['total_rainfall_mm'] < 0).sum()
zero_rainfall = (weather_cleaned_df['total_rainfall_mm'] == 0).sum()
print(f"   Negative rainfall values: {negative_rainfall}")
print(f"   Zero rainfall values: {zero_rainfall}")
print(f"   Minimum rainfall: {weather_cleaned_df['total_rainfall_mm'].min()}")
print(f"   Maximum rainfall: {weather_cleaned_df['total_rainfall_mm'].max()}")

# 8. Temperature validation
print("\n8. Temperature Validation:")
temp_below_20 = (weather_cleaned_df['mean_temperature_c'] < 20).sum()
temp_above_35 = (weather_cleaned_df['mean_temperature_c'] > 35).sum()
print(f"   Temperature below 20°C: {temp_below_20}")
print(f"   Temperature above 35°C: {temp_above_35}")
print(f"   Minimum temperature: {weather_cleaned_df['mean_temperature_c'].min()}")
print(f"   Maximum temperature: {weather_cleaned_df['mean_temperature_c'].max()}")

# Check date range
print("\n6. Check date range:") 
print(f"First record month: {weather_cleaned_df['record_month'].min()}")
print(f"First year: {weather_cleaned_df['year'].min()}")
print(f"First month_number: {weather_cleaned_df['month_number'].min()}")
print(f"Last record month: {weather_cleaned_df['record_month'].max()}")
print(f"Last year: {weather_cleaned_df['year'].max()}")
print(f"Last month_number: {weather_cleaned_df['month_number'].max()}")

# Check data type
print("\n7. Check data types:")
print(f"Data types: {weather_cleaned_df.dtypes}")

# Check columns name
print("\n8. Check columns name:")
print(f"Column name: {weather_cleaned_df.columns.tolist()}")

print("\n" + "-" * 60)
print("VALIDATING COMPLETED")
print("-" * 60)