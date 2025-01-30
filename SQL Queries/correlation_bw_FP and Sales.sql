--correlation between fuel price and sales
select fuel_price, avg(weekly_sales) as Avg_WS
from walmart_sales_analysis
group by fuel_price
order by fuel_price;
