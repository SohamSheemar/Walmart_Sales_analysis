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


#impact of unemployement on sales

# Group by unemployment and calculate average weekly sales
unemployement_sales = df.groupby('unemployement')['weekly_sales'].mean().reset_index()

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(unemployement_sales['unemployement'], unemployement_sales['weekly_sales'], color='b')
plt.title('Impact of Unemployment on Weekly Sales')
plt.xlabel('Unemployment Rate')
plt.ylabel('Average Weekly Sales')
plt.grid()
plt.show()