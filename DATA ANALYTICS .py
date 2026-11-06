
# CAREBRIDGE - Healthcare Data Analytics and Visualization

import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load dataset
df = pd.read_csv("DATA_COLLECTION_cleaned.csv")

# Create output folder
os.makedirs("Healthcare_Graphs", exist_ok=True)

# Convert date columns
df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"], errors="coerce"
)

# 2. Basic Data Analytics
print("\n========== HEALTHCARE DATA ANALYTICS ==========")

print("\nDataset Information:")
print(df.info())

print("\nTotal Patient Records:")
print(len(df))

print("\nUnique Patients:")
print(df["Patient_ID"].nunique())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Analysis:")
print(df.describe())

print("\nDisease Distribution:")
print(df["Disease"].value_counts())

print("\nAverage Treatment Cost:")
print(df["Total_Cost_INR"].mean())

print("\nTotal Treatment Cost:")
print(df["Total_Cost_INR"].sum())

print("\nAverage Hospital Stay:")
print(df["Length_of_Stay_Days"].mean())


# 3. Patients by Medical Condition
plt.figure(figsize=(10, 6))

df.groupby("Disease")["Patient_ID"].nunique().sort_values().plot(
    kind="barh"
)

plt.title("Patients by Medical Condition")
plt.xlabel("Number of Patients")
plt.ylabel("Medical Condition")
plt.tight_layout()
plt.savefig("Healthcare_Graphs/1_Patients_by_Condition.png")
plt.show()


# 4. Average Treatment Cost by Condition
plt.figure(figsize=(10, 6))

df.groupby("Disease")["Total_Cost_INR"].mean().sort_values().plot(
    kind="bar", color="skyblue"
)

plt.title("Average Treatment Cost by Condition")
plt.xlabel("Medical Condition")
plt.ylabel("Average Cost (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Healthcare_Graphs/2_Treatment_Cost.png")
plt.show()


# 5. Patient Recovery Status
plt.figure(figsize=(8, 6))

df["Recovery_Status"].value_counts().plot(
    kind="pie", autopct="%1.1f%%"
)

plt.title("Patient Recovery Status")
plt.ylabel("")
plt.tight_layout()
plt.savefig("Healthcare_Graphs/3_Patient_Outcome.png")
plt.show()


# 6. Readmission Risk Analysis
plt.figure(figsize=(9, 6))

df.groupby("Patient_Risk_Level")["Readmission_Risk"].mean().plot(
    kind="bar", color="orange"
)

plt.title("Average Readmission Risk by Patient Risk Level")
plt.xlabel("Patient Risk Level")
plt.ylabel("Average Readmission Risk")
plt.tight_layout()
plt.savefig("Healthcare_Graphs/4_Readmission_Risk.png")
plt.show()


# 7. Doctor Performance
plt.figure(figsize=(10, 6))

df.groupby("Doctor_ID")["Patient_ID"].nunique().nlargest(10).sort_values().plot(
    kind="barh", color="green"
)

plt.title("Top 10 Doctors by Patient Caseload")
plt.xlabel("Number of Patients")
plt.ylabel("Doctor ID")
plt.tight_layout()
plt.savefig("Healthcare_Graphs/5_Doctor_Performance.png")
plt.show()


# 8. Monthly Patient Admissions
monthly = (
    df.dropna(subset=["Admission_Date"])
      .set_index("Admission_Date")
      .resample("MS")["Patient_ID"]
      .nunique()
)

plt.figure(figsize=(10, 6))

monthly.plot(kind="line", marker="o")

plt.title("Monthly Patient Admissions")
plt.xlabel("Month")
plt.ylabel("Number of Patients")
plt.grid()
plt.tight_layout()
plt.savefig("Healthcare_Graphs/6_Monthly_Admissions.png")
plt.show()


# 9. Department-wise Patient Analysis
plt.figure(figsize=(10, 6))

df.groupby("Department")["Patient_ID"].nunique().sort_values().plot(
    kind="barh", color="purple"
)

plt.title("Patients by Hospital Department")
plt.xlabel("Number of Patients")
plt.ylabel("Department")
plt.tight_layout()
plt.savefig("Healthcare_Graphs/7_Department_Analysis.png")
plt.show()


# 10. Disease Severity Analysis
plt.figure(figsize=(8, 6))

df["Disease_Severity"].value_counts().plot(
    kind="bar", color="coral"
)

plt.title("Patient Count by Disease Severity")
plt.xlabel("Disease Severity")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.savefig("Healthcare_Graphs/8_Disease_Severity.png")
plt.show()


print("\n========== ANALYTICS COMPLETED ==========")
print("All graphs saved in Healthcare_Graphs folder.")
