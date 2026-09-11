import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"Dataset\superstore_sales_analysis_cleaned.csv")

# Calculate sales by region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

# Create visualization
plt.figure(figsize=(9, 6))
plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# Save chart
plt.savefig(
    r"Visualizations\sales_by_region.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()