# **Walmart Sales Analysis Project**

## **Overview**
This project analyzes Walmart sales data to uncover trends, patterns, and insights that can help improve business performance. The dataset includes information about weekly sales, store details, holiday flags, temperature, fuel prices, CPI, and unemployment rates. The analysis is performed using **PostgreSQL** for data querying and **Python** (Pandas, Matplotlib, Seaborn) for data visualization.

---

## **Dataset**
The dataset used in this project is the **Walmart Sales Dataset** from Kaggle. It contains the following columns:
- `Store`: Store ID.
- `Date`: Week of sales.
- `Weekly_Sales`: Sales for the given store and date.
- `Holiday_Flag`: Whether the week is a holiday week (1 = holiday, 0 = non-holiday).
- `Temperature`: Average temperature in the region.
- `Fuel_Price`: Cost of fuel in the region.
- `CPI`: Consumer Price Index.
- `Unemployment`: Unemployment rate.

Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mikhail1681/walmart-sales/data).

---

## **Project Structure**
```
walmart-sales-analysis/
├── data/
│   └── Walmart.csv                # Raw dataset
├── scripts/
│   ├── sql_queries.sql            # SQL queries for analysis
│   ├── data_analysis.py           # Python script for analysis and visualization
├── results/
│   ├── monthly_sales_trend.png    # Sample visualization
│   └── total_sales_by_store.png   # Sample visualization
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

---

## **Steps to Reproduce the Project**

### **1. Set Up the Database**
1. Install PostgreSQL and create a database:
   ```sql
   CREATE DATABASE walmart_sales;
   ```

2. Create the `walmart_sales_analysis` table:
   ```sql
   CREATE TABLE walmart_sales_analysis (
       store_id INT,
       date DATE,
       weekly_sales NUMERIC(10, 2),
       holiday_flag INT,
       temperature NUMERIC(10, 2),
       fuel_price NUMERIC(10, 2),
       cpi NUMERIC(10, 2),
       unemployment NUMERIC(10, 2),
       PRIMARY KEY (store_id, date)
   );
   ```

3. Load the dataset into the table:
   ```sql
   COPY walmart_sales_analysis(store_id, date, weekly_sales, holiday_flag, temperature, fuel_price, cpi, unemployment)
   FROM '/path/to/Walmart.csv'
   DELIMITER ','
   CSV HEADER;
   ```

---

### **2. Run SQL Queries**
Example SQL queries for analysis are provided in `SQL Queries/`. Some key queries include:
- Total sales by store.
- Average weekly sales by holiday flag.
- Monthly sales trend.
- Correlation between unemployment and sales.

---

### **3. Analyze and Visualize Data**
- Install all the required Python dependencies and visualise the data
---

### **4. Key Visualizations**
- **Total Sales by Store**: Bar plot showing total sales for each store.
- **Monthly Sales Trend**: Line plot showing sales trends over time.
- **Impact of Holidays on Sales**: pie plot comparing sales during holiday vs. non-holiday weeks.
- **Correlation Between Unemployment and Sales**: Scatter plot showing the relationship.
- **Sales by Top 5 Stores**: Pie plot showing percent sales of top 5 stores
- **Correlation Between Temperature and Sales**: Scatter plot showing the relationship
- **Correlation Between Fuel Prices and Sales**: Line plot showing the relationship
- **Correlation Matrix**

---

## **Requirements**
- PostgreSQL
- Python 3.x
- Libraries: `pandas`, `matplotlib`, `seaborn`, `psycopg2`

Install the required Python libraries using:
```bash
pip install pandas matplotlib seaborn psycopg2
```

---

## **Results**
The analysis reveals:
- Stores with the highest and lowest sales.
- Seasonal trends in sales.
- The impact of holidays, temperature, fuel prices, and unemployment on sales.

Visualizations are saved in the `Figures/` folder.

---

## **Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---
