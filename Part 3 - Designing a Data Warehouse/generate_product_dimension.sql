-- Creating the dwh_products table
drop table if exists dwh_products;

create table dwh_products as
select *
from whiskey_retail_shop.products 
order by product_id;

-- Setting product_id as the primary key
alter table dwh_products
modify column product_id int not null primary key;
