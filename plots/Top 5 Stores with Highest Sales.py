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


#Top 5 Stores with Highest Sales

# Group by store and calculate total sales, then get top 5
top_stores = df.groupby('store_id')['weekly_sales'].sum().nlargest(5).reset_index()

top_5_stores = top_stores.nlargest(5, 'weekly_sales')

# Convert store_id to string for labeling
store_labels = top_5_stores['store_id'].astype(str)

# Plot pie chart
plt.figure(figsize=(10, 6))
plt.pie(top_5_stores['weekly_sales'], labels=store_labels, 
        colors=['teal', 'magenta', 'lightgreen', 'lightyellow', 'red'], autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Stores with Highest Sales')
plt.legend()
plt.show()