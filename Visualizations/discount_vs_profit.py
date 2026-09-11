import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"Dataset\superstore_sales_analysis_cleaned.csv")

# Create scatter plot
plt.figure(figsize=(9, 6))
plt.scatter(df["Discount"], df["Profit"], alpha=0.35)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid(alpha=0.3)
plt.tight_layout()

# Save chart
plt.savefig(
    r"Visualizations\discount_vs_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()