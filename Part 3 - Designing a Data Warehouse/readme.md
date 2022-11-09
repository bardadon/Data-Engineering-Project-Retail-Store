# Part 3 - Designing a Data Warehouse
In this part, I will design a Data Warehouse which will be the main analytic focal point of the company. 

I'll create a fact table and various dimensions for the Data Warehouse such as Date, Customers, Employees, Paymnets and Products Dimension.

I will also create multiple triggers that will handle the transfer of data between the company's central Database and the Data Warehouse.

## Applying the code

### In Python - Generate the Date Dimension

```
python generate_date_dimension.py
```

### In MySQL - Generate Dimensions & Triggers

```
generate_customers_dimension.sql
generate_employee_dimension.sql
generate_product_dimension.sql
generate_fact_table.sql

triggers.sql
```
### Finished Data Warehouse Schema:
![1 6V1ZTROGwoa9IKy1DDrDtg](https://user-images.githubusercontent.com/65648983/200848563-b557b0a7-1889-4f87-811e-0c7a98cb0ed9.png)
