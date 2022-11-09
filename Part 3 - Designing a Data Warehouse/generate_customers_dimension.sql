-- Creating the dwh_customers table
drop table if exists dwh_customers;

create table dwh_customers as
select 
	c1.customer_id,
    c1.first_name,
    c1.last_name,
    c1.full_name,
    c2.country_code
from whiskey_retail_shop.customers as c1
join whiskey_retail_shop.countries as c2
on c1.country_id = c2.country_id
order by customer_id;

-- Setting customer_id as the primary key
alter table dwh_customers
modify column customer_id int not null primary key;
