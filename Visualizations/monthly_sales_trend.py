import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"Dataset\superstore_sales_analysis_cleaned.csv")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Aggregate monthly sales
monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

# Convert period to timestamp for plotting
monthly_sales.index = monthly_sales.index.to_timestamp()

# Create visualization
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save chart
plt.savefig(
    r"Visualizations\monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()