-- Create a new fact table: dwh_fact
drop table if exists dwh_fact;

CREATE TABLE dwh_fact AS 
SELECT c1.customer_id,
    e1.employee_id,
    p2.product_id,
    p2.Alcohol_Amount,
    p2.Alcohol_Percent,
    p2.Alcohol_Price,
    p2.Product_Name,
    c1.four_digits,
    c2.Country,
    c3.credit_provider,
    d.Date_key,
    p1.date 
FROM
    whiskey_retail_shop.payments AS p1
        JOIN
    whiskey_retail_shop.customers AS c1 ON p1.customer_id = c1.customer_id
        JOIN
    whiskey_retail_shop.employees AS e1 ON p1.employee_id = e1.employee_id
        JOIN
    whiskey_retail_shop.products AS p2 ON p1.product_id = p2.product_id
        JOIN
    whiskey_retail_shop.countries AS c2 ON c1.country_id = c2.country_id
        JOIN
    whiskey_retail_shop.customer_cc AS c3 ON c1.credit_provider_id = c3.credit_provider_id
        JOIN
    dwh_date AS d ON p1.date = d.Dates
ORDER BY d.Dates;

-- Setting the foreign keys for each dimension table
alter table dwh_fact
add foreign key (customer_id)  references dwh_customers ( customer_id);

alter table dwh_fact
add foreign key (employee_id)  references dwh_employees ( employee_id);

alter table dwh_fact
add foreign key (product_id)  references dwh_products ( product_id);

alter table dwh_fact
add foreign key (Date_key)  references dwh_date ( Date_key);
