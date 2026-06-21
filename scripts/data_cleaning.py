import pandas as pd

print("===================================")
print("Educational Dataset Cleaning Tool")
print("===================================")

# Load datasets

student_df = pd.read_csv("data/raw/csv/student_performance.csv")
qa_df = pd.read_csv("data/raw/csv/educational_qa.csv")

print("\nDatasets Loaded Successfully")

# ---------------------------------
# Student Performance Dataset
# ---------------------------------

print("\nChecking student_performance.csv")

print("\nMissing Values:")
print(student_df.isnull().sum())

print("\nDuplicate Records:")
print(student_df.duplicated().sum())

student_df = student_df.drop_duplicates()

student_df.to_csv(
    "data/cleaned/cleaned_student_performance.csv",
    index=False
)

print("\nCleaned student_performance.csv saved")

# ---------------------------------
# Educational QA Dataset
# ---------------------------------

print("\nChecking educational_qa.csv")

print("\nMissing Values:")
print(qa_df.isnull().sum())

print("\nDuplicate Records:")
print(qa_df.duplicated().sum())

qa_df = qa_df.drop_duplicates()

qa_df.to_csv(
    "data/cleaned/cleaned_educational_qa.csv",
    index=False
)

print("\nCleaned educational_qa.csv saved")

print("\n===================================")
print("Data Cleaning Completed Successfully")
print("===================================")