import pandas as pd
import numpy as np

# 1. Loading Data
file_path = "sample_-_superstore.xls"
df = pd.read_excel(file_path)
print("Original Shape:", df.shape)

# 2. Data Cleaning
# Remove duplicate rows
df = df.drop_duplicates()

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Handle missing values
numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
print("After Cleaning Shape:", df.shape)

# 3. Feature Engineering
# Time Features
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.strftime('%b')
df['Quarter'] = df['Order Date'].dt.quarter

# Shipping Performance
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Profit Margin
df['Profit Margin'] = np.where(df['Sales'] != 0, df['Profit'] / df['Sales'], 0)

# Discount Category
df['Discount Level'] = np.where(df['Discount'] > 0.3, 'High', 'Low')

# Sales Category
df['Sales Segment'] = pd.qcut(df['Sales'],q=3,labels=['Low', 'Medium', 'High'])

# 4. Aggregated Tables for Analysis
# Monthly Sales Trend
monthly_sales = df.groupby(['Year', 'Month', 'Month Name'])[['Sales', 'Profit']].sum().reset_index()

# Category Performance
category_summary = df.groupby(['Category', 'Sub-Category'])[['Sales', 'Profit', 'Quantity']].sum().reset_index()

# Regional Performance
print(df.columns.tolist())
region_summary = df.groupby(['Region', 'State/Province'])[['Sales', 'Profit']].sum().reset_index()

# Customer Analysis
customer_summary = df.groupby('Customer Name')[['Sales', 'Profit']].sum().reset_index()
customer_summary = customer_summary.sort_values(by='Sales', ascending=False)

# Loss Analysis
loss_summary = df[df['Profit'] < 0]
loss_summary = loss_summary.groupby('Sub-Category')[['Sales', 'Profit']].sum().reset_index()

# Shipping Analysis
shipping_summary = df.groupby('Region')['Shipping Days'].mean().reset_index()

# 5. Handling Outlier Data

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Sales'] >= Q1 - 1.5 * IQR) &
        (df['Sales'] <= Q3 + 1.5 * IQR)]


output_file = "superstor_Cleaned_data.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    
    # Main cleaned data
    df.to_excel(writer, sheet_name='Cleaned_Data', index=False)
    
    # Other tables
    monthly_sales.to_excel(writer, sheet_name='Monthly_Sales', index=False)
    category_summary.to_excel(writer, sheet_name='Category_Summary', index=False)
    region_summary.to_excel(writer, sheet_name='Region_Summary', index=False)
    customer_summary.to_excel(writer, sheet_name='Customer_Summary', index=False)
    loss_summary.to_excel(writer, sheet_name='Loss_Summary', index=False)
    shipping_summary.to_excel(writer, sheet_name='Shipping_Summary', index=False)
print("Excel file created: superstore_analysis.xlsx")