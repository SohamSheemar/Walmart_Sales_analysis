create table walmart_sales_analysis (
store_id int,
date DATE,
weekly_sales numeric(10,2),
holiday_flag int,
temperature numeric(10,2),
fuel_price numeric(10,2),
cpi numeric(10,2),
unemployement numeric(10,2),
primary key (store_id, date)
);