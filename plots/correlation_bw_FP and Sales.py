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


#correlation between fuel and sales

# Group by fuel_price and calculate average weekly sales
fuel_sales = df.groupby('fuel_price')['weekly_sales'].mean().reset_index()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(fuel_sales['fuel_price'], fuel_sales['weekly_sales'], marker='o', color='g')
plt.title('Correlation Between Fuel Price and Weekly Sales')
plt.xlabel('Fuel Price')
plt.ylabel('Average Weekly Sales')
plt.grid()
plt.show()