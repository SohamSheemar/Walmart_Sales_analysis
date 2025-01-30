--average weekly sales by holiday_flag
select holiday_flag, avg(weekly_sales) as average_WS
from walmart_sales_analysis
group by holiday_flag;
