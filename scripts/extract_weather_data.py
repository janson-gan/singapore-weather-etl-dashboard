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

# Display rainfall information
print("Rainfall loaded successfully.")
print("Rainfall rows and columns:", rainfall_df.shape)
print("Rainfall columns:", rainfall_df.columns.tolist())
print(rainfall_df.head())

print("\n" + "-" * 50 + "\n")

# Display temperature information
print("Temperature loaded successfully.")
print("Temperature rows and columns:", temperature_df.shape)
print("Temperature columns:", temperature_df.columns.tolist())
print(temperature_df.head())