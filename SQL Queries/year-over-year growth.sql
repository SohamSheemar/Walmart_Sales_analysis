WITH monthly_sales AS (
  SELECT DATE_TRUNC('year', date) AS year, SUM(weekly_sales) AS total_sales
  FROM walmart_sales_analysis
  GROUP BY year
)
SELECT year, total_sales, LAG(total_sales) OVER (ORDER BY year) AS prev_year_sales,
       (total_sales - LAG(total_sales) OVER (ORDER BY year)) / LAG(total_sales) OVER (ORDER BY year) * 100 AS growth_percent
FROM monthly_sales;