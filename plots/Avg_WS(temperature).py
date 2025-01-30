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


#impact of temperature on sales

# Group by temperature and calculate average weekly sales
temp_sales = df.groupby('temperature')['weekly_sales'].mean().reset_index()

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(temp_sales['temperature'], temp_sales['weekly_sales'], color='purple')
plt.title('Impact of Temperature on Weekly Sales')
plt.xlabel('Temperature (°F)')
plt.ylabel('Average Weekly Sales')
plt.grid()
plt.show()