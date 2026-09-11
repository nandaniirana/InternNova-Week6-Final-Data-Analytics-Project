\# Exploratory Data Analysis



\## 1. Dataset Overview



The cleaned Superstore sales dataset was used for the exploratory data analysis.



\- Rows: 10,194

\- Columns: 21

\- Missing values: 0

\- Duplicate rows: 0

\- Numerical measures: Sales, Quantity, Discount, Profit

\- Date fields: Order Date, Ship Date

\- Key categorical fields: Category, Sub-Category, Region, Segment, Ship Mode



The dataset was inspected before analysis to confirm its structure, data types, completeness, and consistency.



\## 2. Data Types



The dataset contains:



\- Integer fields: Row ID, Quantity

\- Floating-point fields: Sales, Discount, Profit

\- Text/categorical fields: Order ID, Ship Mode, Customer ID, Customer Name, Segment, Region, Category, Sub-Category, Product ID, Product Name, and location fields

\- Date fields: Order Date and Ship Date



Both Order Date and Ship Date were successfully validated as convertible to valid dates.



\## 3. Data Quality and Cleaning



The dataset was checked for missing values and duplicate records.



\- Missing values: 0

\- Duplicate rows: 0

\- Invalid Order Date values: None detected

\- Invalid Ship Date values: None detected



Since the dataset was already complete and consistent, no imputation or duplicate removal was required.



\## 4. Descriptive Statistics



Key descriptive statistics were calculated for the main numerical variables.



| Metric | Sales | Quantity | Discount | Profit |

|---|---:|---:|---:|---:|

| Mean | 228.23 | 3.79 | 0.16 | 28.67 |

| Standard Deviation | 619.91 | 2.23 | 0.21 | 232.47 |

| Minimum | 0.44 | 1.00 | 0.00 | -6599.98 |

| 25th Percentile | 17.22 | 2.00 | 0.00 | 1.76 |

| Median | 53.91 | 3.00 | 0.20 | 8.69 |

| 75th Percentile | 209.50 | 5.00 | 0.20 | 29.30 |

| Maximum | 22638.48 | 14.00 | 0.80 | 8399.98 |



Sales and Profit show substantial variation, with values extending considerably above their medians.



\## 5. Correlation Analysis



The Pearson correlation matrix was used to examine relationships between the main numerical variables.



\- Sales and Profit: 0.48

\- Sales and Quantity: 0.20

\- Sales and Discount: -0.03

\- Quantity and Profit: 0.07

\- Discount and Profit: -0.22



The strongest relationship observed was between Sales and Profit, with a moderate positive correlation of 0.48.



Discount and Profit showed a negative correlation of -0.22, suggesting that higher discounts are associated with lower profitability in the dataset.



\## 6. Outlier Analysis



The Interquartile Range (IQR) method was used to identify potential outliers.



\- Sales outliers: 1,183

\- Profit outliers: 1,913



These observations were retained because extreme sales and profit values can represent genuine business transactions and may contain useful business information.



\## 7. Category Analysis



Category-level Sales and Profit were analyzed.



| Category | Sales | Profit |

|---|---:|---:|

| Furniture | 754,747.76 | 19,730.00 |

| Office Supplies | 738,193.31 | 126,023.44 |

| Technology | 839,893.28 | 146,543.38 |



Technology generated the highest sales and the highest profit among the three categories.



Furniture generated substantial sales but comparatively low profit, indicating an opportunity to examine its pricing, discounting, and product-level profitability.



\## 8. Regional Analysis



Regional Sales and Profit were analyzed to identify high- and low-performing regions.



| Region | Sales | Profit |

|---|---:|---:|

| Central | 503,170.67 | 39,865.31 |

| East | 691,828.17 | 94,883.26 |

| South | 391,721.90 | 46,749.43 |

| West | 739,813.61 | 110,798.82 |



The West region generated the highest Sales and Profit, while the South region had the lowest Sales.



\## 9. Time-Based Analysis



Monthly Sales and Profit were analyzed across the available Order Date periods.



The analysis shows that sales and profitability vary considerably across months. Later periods contain several high-sales months.



Key observations include:



\- Highest monthly Sales: November 2026 — 118,454.78

\- Highest monthly Profit: December 2025 — 17,926.30

\- Lowest monthly Sales: February 2023 — 4,519.89

\- Lowest monthly Profit: July 2023 — -8,441.48



The monthly analysis indicates seasonal and period-based variation in both sales and profitability.



\## 10. Key EDA Findings



1\. The dataset contains 10,194 records with no missing values or duplicate rows.

2\. Technology is the strongest category based on both Sales and Profit.

3\. The West region is the highest-performing region for both Sales and Profit.

4\. Sales and Profit have a moderate positive correlation of 0.48.

5\. Discount has a negative correlation with Profit (-0.22), highlighting the importance of discount management.

6\. Profit contains more identified IQR outliers than Sales, with 1,913 potential outliers.

7\. Monthly performance varies substantially, with particularly strong results in some later periods.



\## 11. EDA Conclusion



The exploratory analysis provides a clear view of sales performance, profitability, regional performance, category contribution, numerical relationships, outliers, and time-based trends.



The findings provide the analytical foundation for the next stages of the project: data visualization, Power BI dashboard development, and business recommendations.

