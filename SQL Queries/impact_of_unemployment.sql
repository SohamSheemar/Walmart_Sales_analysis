--impact of unemployment on sales
select unemployement,
avg(weekly_sales) as avg_total_sales
from walmart_sales_analysis
group by unemployement
order by unemployement;
