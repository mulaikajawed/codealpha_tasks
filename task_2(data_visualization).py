# =============================
# CodeAlpha Internship Task
# Task 3: Data Visualization
# Dataset: salesdata.csv
# =============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("salesdata.csv")

# Style
sns.set(style="whitegrid")

# Purchase Type Distribution
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Purchase Type")
plt.title("Purchase Type Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("purchase_type_distribution.png")
plt.close()

# Payment Method Distribution
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Payment Method")
plt.title("Payment Method Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("payment_method_distribution.png")
plt.close()

# Total Quantity Sold by Product
plt.figure(figsize=(10,6))
sns.barplot(data=df, x="Product", y="Quantity", estimator=sum, ci=None)
plt.title("Total Quantity Sold by Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("quantity_by_product.png")
plt.close()

# Total Sales by City
df["Total_Sales"] = df["Price"] * df["Quantity"]
plt.figure(figsize=(10,6))
sns.barplot(data=df, x="City", y="Total_Sales", estimator=sum, ci=None)
plt.title("Total Sales by City")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_sales_by_city.png")
plt.close()

print("\n✅ Data Visualizations saved as PNG files in the current folder.")
