import numpy as np
import pandas as pd
import names
from faker import Faker
faker = Faker()
import pandasql as ps
import random
import time
from datetime import datetime

def sql(query):
    return ps.sqldf(query)

# Import the whisky_web_scraping class
from Helper import whisky_web_scraping

# Create a scraper object
scraper = whisky_web_scraping()

'''
Generating Product Data
'''

# Scrape Data
product_df = scraper.scrape_whisky(number_of_pages=5)

# Changing the Alcohol Price to float
product_df['Alcohol_Price'] = product_df.Alcohol_Price.str.replace(',','').astype('float')

# Generate a column of unique product ids
product_id = np.random.default_rng().choice(len(product_df.Product_Name), len(product_df.Product_Name), replace = False)

# Verify that there are as many ids as there are products
assert len(set(product_id)) == len(product_df.Product_Name)

# Verify that the new ids are unique
assert len(pd.Series(product_id).unique()) == len(product_id)

# Insert the new column into the dataframe
product_df['product_id'] = product_id


'''
Generating Employee Data
'''

# Generating 100 Employee Unique id's
employee_id = np.random.default_rng().choice(4000, 100, replace = False)

# Verify that there are as many ids as there are employees
assert len(set(employee_id)) == 100

# Verify that the new ids are unique
assert len(pd.Series(employee_id).unique()) == len(employee_id)

# Generating 100 Employee Data
employee_first_name = []
employee_last_name = []
employee_full_name = []
employee_email = []
employee_city = []
departments = ['Sales', 'Finance', 'Marketing', 'BI']
employee_department = []

# iterate through the employees and generate random data
for i in range(len(employee_id)):
    employee_first_name.append(names.get_first_name())
    employee_last_name.append(names.get_last_name())
    employee_full_name.append(employee_first_name[i] + ' ' + employee_last_name[i])
    employee_email.append(employee_first_name[i] + employee_last_name[i][0].lower() + '@gmail.com')
    employee_city.append(faker.city())
    employee_department.append(np.random.choice(departments, 1)[0])
    
# Create an employee dataframe
employee_df = pd.DataFrame(employee_id, columns = ['employee_id'])
employee_df['first_name'] = employee_first_name
employee_df['last_name'] = employee_last_name
employee_df['full_name'] = employee_full_name
employee_df['email'] = employee_email
employee_df['city'] = employee_city
employee_df['department'] = employee_department
    
    
'''
Generating Customer Data
'''

# Generating 1000 Customer Unique id's
customer_id = np.random.default_rng().choice(999999, 1000, replace = False)

# Verify that there are as many ids as there are customers
assert len(set(customer_id)) == 1000

# Verify that the new ids are unique
assert len(pd.Series(customer_id).unique()) == len(customer_id)

# Generating 1000 Customers Data
customer_first_name = []
customer_last_name = []
customer_full_name = []
customer_email = []
customer_last_four_digits = []
customer_country = []
customer_country_code = []
customer_street = []
customer_credit_card_company = []


# iterate through the customers and generate random data
for i in range(len(customer_id)): 
    customer_first_name.append(names.get_first_name())
    customer_last_name.append(names.get_last_name())
    customer_full_name.append(customer_first_name[i] + ' ' + customer_last_name[i])
    customer_email.append(customer_first_name[i] + customer_last_name[i][0].lower() + '@gmail.com')
    customer_last_four_digits.append(np.random.randint(low = 1000, high = 9999, size = 1)[0])
    customer_country.append(faker.country())
    customer_country_code.append(customer_country[i][0:3].upper())
    customer_street.append(faker.street_address())
    customer_credit_card_company.append(faker.credit_card_provider())
    
# Create a customer dataframe
customer_df = pd.DataFrame(customer_id, columns = ['customer_id'])
customer_df['first_name'] = customer_first_name
customer_df['last_name'] = customer_last_name
customer_df['full_name'] = customer_full_name
customer_df['email'] = customer_email
customer_df['country'] = customer_country
customer_df['country_code'] = customer_country_code
customer_df['street'] = customer_street
customer_df['credit_provider'] = customer_credit_card_company
customer_df['four_digits'] = customer_last_four_digits

    
'''
Generating Payments Data
'''
# Generating random days in the range of 1990 to 2020
date_range = pd.date_range(start = "1990-01-01", end = "2020-12-31", freq="D")

# Generating Unique payment id's
payment_id = np.random.default_rng().choice(999999, len(date_range), replace = False)

# Verify that there are as many ids as there are dates
assert len(set(payment_id)) == len(date_range)

# Verify that the new ids are unique
assert len(pd.Series(payment_id).unique()) == len(payment_id)

# Generating payments Data
customer_id_payments = []
employee_id_payments = []
product_id_payments = []
dates = []


# iterate through the payments and generate random data
for i in range(len(payment_id)):
    dates.append(datetime.strftime(random.choice(date_range), format='%Y-%m-%d'))
    customer_id_payments.append(random.choice(customer_id))
    employee_id_payments.append(random.choice(employee_id))
    product_id_payments.append(random.choice(product_id))
    
# Create a payments dataframe
payment_df = pd.DataFrame(payment_id, columns = ['payment_id'])
payment_df['date'] = sorted(dates)
payment_df['customer_id'] = customer_id_payments
payment_df['employee_id'] = employee_id_payments
payment_df['product_id'] = product_id_payments



# Adding the Alcohol_price column to the table
query = '''
select p1.*, p2.Alcohol_Price as price
from payment_df p1
inner join product_df p2
on p1.product_id = p2.product_id
'''

payment_df = sql(query)
