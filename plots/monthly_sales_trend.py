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


#correlation between month and sales

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by month and calculate total sales
df['month'] = df['date'].dt.to_period('M')
monthly_sales = df.groupby('month')['weekly_sales'].sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['month'].astype(str), monthly_sales['weekly_sales'], marker='o', color='blue')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid()
plt.show()