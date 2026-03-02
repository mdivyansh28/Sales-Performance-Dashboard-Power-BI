# Sales Performance Analysis & Dashboard (Python + Power BI)

## Project Overview

This project presents an end-to-end data analysis workflow, starting from raw retail transaction data to the development of an interactive Power BI dashboard. The objective was to clean, transform, and structure the data using Python, and then build a business-focused dashboard to analyze sales performance, profitability, customer behavior, and operational efficiency.

The dataset contains over 10,000 transaction records including order details, customer information, product categories, regional data, discounts, sales, and profit.


## Project Workflow

### 1. Data Cleaning & Preparation (Python – Pandas, NumPy)

Raw data was processed using Python to ensure accuracy, consistency, and usability for analysis.

**Cleaning steps performed:**

* Removed duplicate records
* Handled missing values in numerical and categorical fields
* Standardized column names and data types
* Converted date columns into proper datetime format

**Feature Engineering:**

* Extracted **Year, Month, and Quarter** from Order Date
* Calculated **Shipping Days** (delivery efficiency)
* Created **Profit Margin** metric
* Segmented **Discount Levels** (High vs Low)
* Removed extreme outliers using the IQR method

The cleaned and structured data was exported into a single Excel file to serve as the data model for Power BI.

### 2. Data Modeling for Visualization

The final Excel file contains:

* Cleaned transactional data
* Aggregated business tables (monthly performance, category summary, regional performance, etc.)

This structure improves performance and enables efficient analysis in Power BI.


### 3. Dashboard Development (Power BI)

An interactive dashboard was built to provide a comprehensive view of business performance.

**Key Components:**

**Executive Cards**

* Total Sales
* Total Profit
* Profit Margin
* Total Orders
* Average Shipping Days

**Trend Analysis**

* Monthly Sales and Profit trends to identify growth patterns and seasonality

**Product Performance**

* Sales distribution by Category and Sub-category
* Identification of high-revenue but low-profit products

**Regional Analysis**

* Sales and profit comparison across regions and states
* Geographic performance insights

**Customer Insights**

* Top customers contributing to revenue
* Revenue concentration analysis (Pareto effect)

**Interactivity**

* Filters for Year, Region, Segment, and Category
* Cross-filtering across visuals for exploratory analysis

## Key Business Insights

* High discount levels increase sales volume but significantly reduce profit margins
* The Technology category contributes the highest share of overall profit
* Sales show seasonal peaks toward the end of the year
* A small group of customers contributes a large portion of total revenue
* Certain product segments generate high sales but low profitability


## Tools & Technologies

* Python (Pandas, NumPy)
* Power BI
* Microsoft Excel

## Repository Contents

* `Sales_Dashboard.pbix` – Interactive Power BI dashboard
* `superstore_cleaned_data.xlsx` – Processed dataset used for analysis
* `dashboard_overview.png` – Dashboard preview
* `README.md` – Project documentation

---

## Project Outcome

This project demonstrates an end-to-end data analytics workflow including data wrangling, feature engineering, data modeling, and business intelligence reporting. The dashboard enables data-driven decision-making by highlighting performance trends, profitability drivers, and operational improvement areas.
