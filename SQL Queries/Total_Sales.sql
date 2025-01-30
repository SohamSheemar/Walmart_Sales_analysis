--total sales by stores
select store_id, sum(weekly_sales) as Total_Sales
from walmart_sales_analysis
group by store_id
order by Total_Sales desc