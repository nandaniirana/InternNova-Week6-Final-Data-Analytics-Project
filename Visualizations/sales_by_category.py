import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"Dataset\superstore_sales_analysis_cleaned.csv")

# Calculate sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

# Create visualization
plt.figure(figsize=(9, 6))
plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# Save chart
plt.savefig(
    r"Visualizations\sales_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()