--top 5 stores with highest sales
select store_id,
sum(weekly_sales) as total_sales
from walmart_sales_analysis
group by store_id
order by total_sales
limit 5;
