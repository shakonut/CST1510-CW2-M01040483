import pandas as pd
from pathlib import Path

df = pd.read_csv(Path("app_final/DATA/cyber_incidents.csv"))

print("=== CSV COLUMN NAMES ===")
print(df.columns)