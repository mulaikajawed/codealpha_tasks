

# CodeAlpha Internship Task
# Task 2: Exploratory Data Analysis (EDA)
# Dataset: salesdata.csv
# =============================

import pandas as pd

# Load Dataset
df = pd.read_csv("salesdata.csv")

# Dataset Shape
print("===== Dataset Shape =====")
print(df.shape)

# Columns
print("\n===== Columns =====")
print(df.columns)

# Data Types
print("\n===== Data Types =====")
print(df.dtypes)

# Null Values
print("\n===== Null Values =====")
print(df.isnull().sum())

# Summary Statistics
print("\n===== Summary Statistics =====")
print(df.describe(include="all").transpose())

# Save EDA Summary to a File
with open("eda_summary.txt", "w", encoding="utf-8") as f:
    f.write("===== Dataset Shape =====\n")
    f.write(str(df.shape) + "\n\n")
    
    f.write("===== Columns =====\n")
    f.write(str(df.columns.tolist()) + "\n\n")
    
    f.write("===== Data Types =====\n")
    f.write(str(df.dtypes.to_dict()) + "\n\n")
    
    f.write("===== Null Values =====\n")
    f.write(str(df.isnull().sum().to_dict()) + "\n\n")
    
    f.write("===== Summary Statistics =====\n")
    f.write(str(df.describe(include='all').transpose()) + "\n\n")

print("\n✅ EDA Completed. Summary saved to eda_summary.txt")
