import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Load Dataset
# =========================
df = pd.read_csv(r"C:\Users\Shubham\OneDrive\Desktop\Python Projects\pandas_env\shopping_behavior_updated.csv")

# =========================
# 1. Trend Analysis
# Average Purchase Amount by Season (Line Chart)
# =========================
season_sales = df.groupby("Season")["Purchase Amount (USD)"].mean()

plt.figure()
plt.plot(season_sales.index, season_sales.values)
plt.title("Average Purchase Amount by Season")
plt.xlabel("Season")
plt.ylabel("Average Purchase Amount (USD)")
plt.show()

# =========================
# 2. Distribution Analysis
# Customer Age Distribution (Histogram)
# =========================
plt.figure()
plt.hist(df["Age"], bins=10)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# =========================
# 3. Comparative Analysis
# Revenue by Product Category (Bar Chart)
# =========================
category_revenue = df.groupby("Category")["Purchase Amount (USD)"].sum()

plt.figure()
plt.bar(category_revenue.index, category_revenue.values)
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue (USD)")
plt.show()

# =========================
# 4. Relationship Analysis
# Previous Purchases vs Purchase Amount (Scatter)
# =========================
plt.figure()
plt.scatter(
    df["Previous Purchases"],
    df["Purchase Amount (USD)"]
)
plt.title("Previous Purchases vs Purchase Amount")
plt.xlabel("Previous Purchases")
plt.ylabel("Purchase Amount (USD)")
plt.show()

# =========================
# 5. Composition Analysis
# Payment Method Distribution (Pie Chart)
# =========================
payment_dist = df["Payment Method"].value_counts()

plt.figure()
plt.pie(
    payment_dist.values,
    labels=payment_dist.index,
    autopct="%1.1f%%"
)
plt.title("Payment Method Distribution")
plt.show()

# =========================
# 6. Customer Satisfaction Analysis
# Review Rating vs Purchase Amount (Scatter)
# =========================
plt.figure()
plt.scatter(
    df["Review Rating"],
    df["Purchase Amount (USD)"]
)
plt.title("Review Rating vs Purchase Amount")
plt.xlabel("Review Rating")
plt.ylabel("Purchase Amount (USD)")
plt.show()

print("Exploratory Data Analysis Completed Successfully.")
