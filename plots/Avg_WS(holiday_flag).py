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


#average weekly sales by holiday flag

# Group by holiday_flag and calculate average weekly sales
holiday_sales = df.groupby('holiday_flag')['weekly_sales'].mean().reset_index()

# Plot
import matplotlib.pyplot as plt

# Aggregate weekly sales by holiday flag
holiday_sales_avg = holiday_sales.groupby('holiday_flag')['weekly_sales'].mean()

# Plot pie chart
plt.figure(figsize=(8, 6))
plt.pie(holiday_sales_avg, labels=['Non-Holiday', 'Holiday'], autopct='%1.1f%%', colors=['lightblue', 'lightgreen'])
plt.title('Average Weekly Sales by Holiday Flag')
plt.show()
