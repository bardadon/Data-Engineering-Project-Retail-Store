'''
Normalizing the Customers Table
'''

# Creating a new table called countries
unique_countries = customer_df.country.unique()
countries_df = pd.DataFrame(unique_countries, columns = ['Country'])
countries_df['Country_Code'] = countries_df.Country.str[0:3]
countries_df['Country_Code'] = countries_df.Country_Code.str.upper()
countries_df['country_id'] = [*range(0,len(countries_df))]

# Extracting the country_id column from customers
query = '''
select countries_df.country_id
from customer_df 
join countries_df
on 
    customer_df.country_code = countries_df.country_code and
    customer_df.country = countries_df.country
'''
country_ids = sql(query)

# Connecting countries to customers by adding the foregin key: country_id
customer_df['country_id'] = country_ids

# Dropping the column country and country_code
customer_df = customer_df.drop(['country','country_code'],axis=1)

# Creating a new table called customer_cc
unique_cc_providers = customer_df.credit_provider.unique()
customer_cc_df = pd.DataFrame(unique_cc_providers, columns = ['credit_provider'])
customer_cc_df['credit_provider_id'] = [*range(0,len(customer_cc_df))]

# Extracting the credit_provider_id column from customers
query = '''
select customer_cc_df.credit_provider_id
from customer_df 
join customer_cc_df
on 
    customer_df.credit_provider = customer_cc_df.credit_provider
'''

credit_provider_id = sql(query)

# Connecting customer_cc to customers by adding the foregin key: credit_provider_id 
customer_df['credit_provider_id'] = credit_provider_id

# Dropping the column credit_provider
customer_df = customer_df.drop(['credit_provider'],axis=1)

'''
Normalizing the Employees Table
'''
# Extracting the departments from the employees table
departments = pd.Series(employee_df.department.unique()).to_list()

# Generating unique department ids
department_id = [*range(0, len(departments))]

# Creating a table called departments
department_df = pd.DataFrame(department_id, columns=['department_id'])
department_df['department'] = departments

# Extracting the country_id column from customers
query = '''
select department_df.department_id
from employee_df 
join department_df
on 
    employee_df.department = department_df.department
'''

department_ids = sql(query)

# Connecting countries to customers by adding the foregin key: country_id
employee_df['department_id'] = department_ids

# Dropping the column department
employee_df = employee_df.drop('department',axis = 1)



