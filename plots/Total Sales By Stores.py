import pandas as pd
import psycopg2
import matplotlib.pyplot as plt


# Database connection parameters
conn = psycopg2.connect(
    dbname="Walmart_Sales",
    user="postgres",
    password="soham0500",
    host="localhost",
    port="5432",
)


query = "SELECT * FROM walmart_sales_analysis;"


df = pd.read_sql(query, conn)


conn.close()


print(df.head())


#total sales by stores

# Group by store and calculate total sales
store_sales = df.groupby('store_id')['weekly_sales'].sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
bar_width = 0.6
plt.bar(store_sales['store_id'], store_sales['weekly_sales'], color='skyblue',width= bar_width )
plt.title('Total Sales by Store')
plt.xlabel('Store ID')
plt.ylabel('Total Sales')

plt.xticks(store_sales['store_id'], rotation=25)

plt.grid(axis='y')
plt.show()