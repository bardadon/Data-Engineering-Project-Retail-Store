# Connecting Python to MySQL
import pymysql
import pandas as pd

'''
1. Connecting Python to MySQL
'''

connection = pymysql.connect(host ='localhost',port=int(3306),user='root',passwd='1365')

# Creating a cursor object
cursor = connection.cursor()

'''
2. Creating a new Schema
'''

# Create a new schema called whiskey_shop
cursor.execute('''
drop schema if exists whiskey_retail_shop;
''')

cursor.execute('''
create schema whiskey_retail_shop;
''')

# Use the new schema
cursor.execute('''
use whiskey_retail_shop;
''')

'''
3. Generating empty tables
'''
# Countries
cursor.execute('''
DROP TABLE IF EXISTS countries;
''')

cursor.execute('''
CREATE TABLE countries (
    Country VARCHAR(100) NOT NULL,
    Country_Code VARCHAR(100) NOT NULL,
    country_id INT PRIMARY KEY
    );
''')

# Customer_cc
cursor.execute('''
DROP TABLE IF EXISTS customer_cc;
''')

cursor.execute('''
CREATE TABLE customer_cc (
    credit_provider VARCHAR(100) NOT NULL,
    credit_provider_id INT PRIMARY KEY
    );
''')

# Products
cursor.execute('''
DROP TABLE IF EXISTS products;
''')

cursor.execute('''
CREATE TABLE products (
    Product_Name VARCHAR(100) NOT NULL,
    Alcohol_Percent FLOAT NOT NULL,
    Alcohol_Amount FLOAT NOT NULL,
    Alcohol_Price FLOAT NOT NULL,
    product_id int NOT NULL PRIMARY KEY
    );
''')

# Departments
cursor.execute('''
DROP TABLE IF EXISTS departments;
''')

cursor.execute('''
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department VARCHAR(100) NOT NULL
    );
''')

# Customers
cursor.execute('''
DROP TABLE IF EXISTS customers;
''')

cursor.execute('''
CREATE TABLE customers (
    customer_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    street VARCHAR(100) NOT NULL,
    four_digits INT NOT NULL,
    country_id INT NOT NULL,
    credit_provider_id INT NOT NULL,
    
    FOREIGN KEY (country_id) REFERENCES countries (country_id),
    FOREIGN KEY (credit_provider_id) REFERENCES customer_cc (credit_provider_id)
);
''')

# Employees
cursor.execute('''
DROP TABLE IF EXISTS employees;
''')

cursor.execute('''
CREATE TABLE employees (
    employee_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
''')

# Payments
cursor.execute('''
DROP TABLE IF EXISTS payments;
''')

cursor.execute('''
CREATE TABLE payments (
    payment_id INT NOT NULL PRIMARY KEY,
    date DATE NOT NULL,
    customer_id INT NOT NULL,
    employee_id INT NOT NULL,
    product_id INT NOT NULL,
    price FLOAT NOT NULL
    );
''')

'''
4. Inserting Data
'''
# Countries
# Convert the Dataframe into a list of arrays
records = countries_df.to_records(index=False)

# Convert the list of arrays into a tuple of tuples
result = tuple(records)

for data in range(0,len(result)):
    
    # Create a new record
    query = "insert into countries (country, country_code, country_id) values {}".format(result[data])
    
    # Execute the query
    cursor.execute(query)
    
    
# Commit the transaction
connection.commit()

# Customer_cc
# Convert the Dataframe into a list of arrays
records = customer_cc_df.to_records(index=False)

# Convert the list of arrays into a tuple of tuples
result = tuple(records)

for data in range(0,len(result)):
    
    # Create a new record
    query = "insert into customer_cc (credit_provider, credit_provider_id) values {}".format(result[data])
    
    # Execute the query
    cursor.execute(query)
    
    
# Commit the transaction
connection.commit()

# Products
# Convert the Dataframe into a list of arrays
records = product_df.to_records(index=False)

# Convert the list of arrays into a tuple of tuples
result = tuple(records)

for data in range(0,len(result)):
    
    # Create a new record
    query = "insert into products (Product_Name, Alcohol_Percent, Alcohol_Amount, Alcohol_Price,product_id) values {}".format(result[data])
    
    # Execute the query
    cursor.execute(query)
    
    
# Commit the transaction
connection.commit()

# Departments
# Convert the Dataframe into a list of arrays
records = department_df.to_records(index=False)

# Convert the list of arrays into a tuple of tuples
result = tuple(records)

for data in range(0,len(result)):
    
    # Create a new record
    query = "insert into departments (department_id, department) values {}".format(result[data])
    
    # Execute the query
    cursor.execute(query)
    
    
# Commit the transaction
connection.commit()

# Customers
# Convert the Dataframe into a list of arrays
records = customer_df.to_records(index=False)

# Convert the list of arrays into a tuple of tuples
result = tuple(records)

for data in range(0,len(result)):
    
    # Create a new record
    query = "insert into customers (customer_id, first_name, last_name, full_name, email, street, four_digits, country_id, credit_provider_id) values {}".format(result[data])
    
    # Execute the query
    cursor.execute(query)
    
    
# Commit the transaction
connection.commit()

# Employees
# Convert the Dataframe into a list of arrays
records = employee_df.to_records(index=False)

# Convert the list of arrays into a tuple of tuples
result = tuple(records)

for data in range(0,len(result)):
    
    # Create a new record
    query = "insert into employees (employee_id, first_name, last_name, full_name,email,city, department_id) values {}".format(result[data])
    
    # Execute the query
    cursor.execute(query)
    
    
# Commit the transaction
connection.commit()

# Payments
# Convert the Dataframe into a list of arrays
records = payment_df.to_records(index=False)

# Convert the list of arrays into a tuple of tuples
result = tuple(records)

for data in range(0,len(result)):
    
    # Create a new record
    query = "insert into payments (payment_id, date,customer_id,employee_id,product_id,price) values {}".format(result[data])
    
    # Execute the query
    cursor.execute(query)
    
    
# Commit the transaction
connection.commit()














