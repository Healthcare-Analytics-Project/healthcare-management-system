"""Clean the hospital patient dataset and save a cleaned CSV."""
from pathlib import Path
import pandas as pd

INPUT = Path(r"C:\Users\ashwa\Downloads\MANI\DATA  COLLECTION.csv")
OUTPUT = Path(__file__).with_name("DATA_COLLECTION_cleaned.csv")

# Preserve identifiers and category values as text; convert measured/count fields below.
df = pd.read_csv(INPUT, dtype={"Patient_ID": "string"})
initial_rows = len(df)

# Standardize headers and remove surrounding whitespace from text fields.
df.columns = df.columns.str.strip()
text_columns = df.select_dtypes(include=["object", "string"]).columns
df[text_columns] = df[text_columns].apply(lambda col: col.str.strip())
df = df.replace(r"^\s*$", pd.NA, regex=True)

# Remove exact duplicate records, then keep the first record for a repeated patient ID.
df = df.drop_duplicates()
if "Patient_ID" in df.columns:
    df = df.drop_duplicates(subset=["Patient_ID"], keep="first")

# Parse numeric fields and dates without inventing values. Unparseable values become missing.
numeric_columns = [
    "Age", "Height_cm", "Weight_kg", "BMI", "BP_Systolic", "BP_Diastolic",
    "Heart_Rate", "Total_Cost_INR", "Readmission_Risk", "Length_of_Stay_Days",
    "Previous_Admissions",
]
for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
for column in ["Admission_Date", "Discharge_Date"]:
    if column in df.columns:
        df[column] = pd.to_datetime(df[column], errors="coerce").dt.strftime("%Y-%m-%d")

# Keep incomplete records visible; no clinical values are imputed or silently altered.
df.to_csv(OUTPUT, index=False, na_rep="")
print(f"Rows: {initial_rows} -> {len(df)}; removed: {initial_rows - len(df)}")
print(f"Saved: {OUTPUT}")
