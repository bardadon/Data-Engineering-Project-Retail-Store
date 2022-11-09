# Create trigger insert_customer
create trigger insert_customer
after insert on whiskey_retail_shop.customers 
for each row
insert into dwh_whiskey.dwh_customers
select 
	c1.customer_id,
    c1.first_name,
    c1.last_name,
    c1.full_name,
    c2.country_code
from customers as c1
join countries as c2
on c1.country_id = c2.country_id
where c1.customer_id = new.customer_id;

# Create trigger insert_employee
create trigger insert_employee
after insert on whiskey_retail_shop.employees 
for each row
insert into dwh_whiskey.dwh_employees
select 
	e.employee_id,
    e.first_name,
    e.last_name,
    e.full_name,
    d.department
from employees as e
join departments as d
on e.department_id = d.department_id
where e.employee_id = new.employee_id;


create trigger new_payment
after insert on payments
for each row
insert into dwh_whiskey.dwh_fact
select 
	c.customer_id,
    e.employee_id,
    pr.product_id,
    pr.Alcohol_Amount,
    pr.Alcohol_Percent,
    pr.Alcohol_Price,
    pr.Product_Name,
    c.four_digits,
    co.Country,
    cc.credit_provider,
    d.Date_key,
    d.Dates
from payments as p
join customers as c
on p.customer_id = c.customer_id
join countries as co
on c.country_id = co.country_id
join customer_cc cc
on c.credit_provider_id = cc.credit_provider_id
join employees e
on p.employee_id = e.employee_id
join products pr
on p.product_id = pr.product_id
join dwh_whiskey.dwh_date d
on d.Dates = p.date
where p.payment_id = new.payment_id;
