--impact of cpi on sales
select cpi,
avg(weekly_sales) as avg_total_sales
from walmart_sales_analysis
group by cpi
order by cpi;
