--impact of temperature on sales
select temperature, avg(weekly_sales) as Avg_WS
from walmart_sales_analysis
group by temperature
order by temperature;
