-- Creating the dwh_customers table
drop table if exists dwh_employees;

create table dwh_employees as
select 
	e.employee_id,
    e.first_name,
    e.last_name,
    e.full_name,
    d.department
from whiskey_retail_shop.employees as e
join whiskey_retail_shop.departments as d
on e.department_id = d.department_id
order by employee_id;

-- Setting employee_id as the primary key
alter table dwh_employees
modify column employee_id int not null primary key;
