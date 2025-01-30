--monthly sales trend
select date_trunc('month', date) as month,
sum(weekly_sales) as monthly_sales
from walmart_sales_analysis
group by month
order by month;
