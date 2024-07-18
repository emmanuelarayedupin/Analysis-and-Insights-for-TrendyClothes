import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = {
    "Product": ["T-Shirt", "Jeans", "Dress", "Jacket", "Sneakers"],
    "Price (?)": [15 * 450, 40 * 450, 30 * 450, 50 * 450, 60 * 450],
    "Sales (units)": [1000, 500, 800, 300, 400],
    "Revenue (?)": [15000 * 450, 20000 * 450, 24000 * 450, 15000 * 450, 24000 * 450],
    "Category": ["Casual", "Casual", "Formal", "Formal", "Casual"],
    "Season": ["Summer", "Winter", "Spring", "Winter", "Summer"]
}

df = pd.DataFrame(data)

# 1. Total Revenue by Product Category
category_revenue = df.groupby('Category')['Revenue (?)'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=category_revenue, x='Category', y='Revenue (?)')
plt.title('Total Revenue by Product Category (?)')
plt.savefig('/mnt/data/total_revenue_by_category_naira.png')
plt.close()

# 2. Total Sales by Season
season_sales = df.groupby('Season')['Sales (units)'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=season_sales, x='Season', y='Sales (units)')
plt.title('Total Sales by Season')
plt.savefig('/mnt/data/total_sales_by_season_naira.png')
plt.close()

# 3. Correlation Between Price and Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Price (?)', y='Sales (units)')
plt.title('Correlation Between Price (?) and Sales')
plt.savefig('/mnt/data/correlation_price_sales_naira.png')
plt.close()

# 4. Revenue per Unit by Product
df['Revenue per Unit (?)'] = df['Revenue (?)'] / df['Sales (units)']

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Product', y='Revenue per Unit (?)')
plt.title('Revenue per Unit by Product (?)')
plt.savefig('/mnt/data/revenue_per_unit_naira.png')
plt.close()

# 5. Average Revenue per Product Category
average_revenue_category = df.groupby('Category')['Revenue (?)'].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=average_revenue_category, x='Category', y='Revenue (?)')
plt.title('Average Revenue per Product Category (?)')
plt.savefig('/mnt/data/average_revenue_per_category_naira.png')
plt.close()
