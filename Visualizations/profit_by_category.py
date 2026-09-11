import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"Dataset\superstore_sales_analysis_cleaned.csv")

# Calculate profit by category
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

# Create visualization
plt.figure(figsize=(9, 6))
plt.bar(category_profit.index, category_profit.values)

plt.title("Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# Save chart
plt.savefig(
    r"Visualizations\profit_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()