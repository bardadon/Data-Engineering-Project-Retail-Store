import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql

plt.style.use('ggplot')
sns.set_palette('Blues_r')
sns.set_context('notebook')

def mysql(query):
    return pd.read_sql_query(query, connection)

def sql(query):
    return ps.sqldf(query)
  
'''
Connecting to MySQL
'''
# Creating a connection object
connection = pymysql.connect(host ='localhost',
                             port=int(3306),
                             user='root',
                             passwd=****,
                             db='dwh_whiskey')

# Creaeting a cursor object
cursor = connection.cursor()

'''
Pulling Data for Analysis
'''
# Creating the query
query = '''
select 
	f.date,
    d.Day_name as Day,
    d.Month_name as Month,
    d.Year_name as Year,
    f.Product_Name,
    f.Alcohol_Price,
    f.Alcohol_Percent,
    f.Alcohol_Amount,
    c.full_name as customer_name,
    co.country as customer_country,
    f.credit_provider,
    e.full_name as employee_name
from dwh_fact as f
left join whiskey_retail_shop.customers c
on f.customer_id = c.customer_id
left join whiskey_retail_shop.countries as co
on co.country_id = c.country_id 
left join dwh_employees as e
on e.employee_id = f.employee_id
left join dwh_date d
on d.Date_key = f.Date_key
order by f.date '''

# Generating a Dataframe according to the query
df = mysql(query)

'''
Pre-Processing
'''
# Extracting a list of column
df_columns = df.columns.to_list()

# Iterating through the columns
for column in df_columns:
    
    # If the column is date, change the data type to datetime
    if column == 'date':
        df[column] = pd.to_datetime(df[column])
    
    # If the column is object, change the data type to category
    if df[column].dtype == 'object':
        df[column] = df[column].astype('category')
        
        
'''
Q1 — Which products produce the most profit?
'''
# Generating a Dataframe containing the 5 most profitable products
query = '''
select 
    count(*) as Number_Of_Transactions, 
    Product_Name, 
    sum(Alcohol_Price) as Profit
    
from df
group by Product_Name
order by sum(Alcohol_Price) desc
limit 5
'''

top_5_products = sql(query)

sns.catplot(data = top_5_products, x = 'Product_Name', y = 'Profit', 
            kind = 'bar', palette='Blues_r', height = 6, aspect = 2)
plt.xlabel('Product Name',size = 16)
plt.xlabel('Profit',size = 16)

plt.title('Top 5 Most Profitable Products',size = 18)

plt.show()

```
Q2 — Which products people usually buy?
```

query = '''
select 
    count(*) as Number_Of_Transactions, 
    Product_Name
    
from df
group by Product_Name
order by count(*) desc
'''

most_bought_products = sql(query)

# Generating a PMF
prob_mass_func = pd.DataFrame(Pmf.from_seq(df.Product_Name))

# Sorting 
sorted_prob_mass_func = prob_mass_func.iloc[:,0].sort_values(ascending = False)

# Filtering only the top 1 percentile of products
sorted_prob_mass_func = sorted_prob_mass_func[sorted_prob_mass_func > sorted_prob_mass_func.quantile(0.99)]

# Generating a Dataframe
probablity_Dataframe = pd.DataFrame()
probablity_Dataframe['Product'] = sorted_prob_mass_func.index
probablity_Dataframe['Probablity to Buy'] = sorted_prob_mass_func.values

# Output
print(probablity_Dataframe)

```
Q3 — Are there any interesting patterns as to when customers like to buy whiskey? If so what are they?
```
query = '''
select 
    count(*) as Number_Of_Transactions, 
    Day
    
from df
group by Day
order by count(*)
'''

most_bought_products_by_day = sql(query)

sns.catplot(data = most_bought_products_by_month, 
            y = 'Number_Of_Transactions', x = 'Month', kind = 'bar',
           height = 6, aspect = 3)
plt.xlabel('Month', size = 18)
plt.ylabel('Number_Of_Transactions', size = 18)
plt.title('Number of Transaction vs Month', size = 22)
plt.show()

'''
Q4 — Are we growing as a company in terms of profits or not?
'''

query = '''
select 
    sum(Alcohol_Price) as Profit, 
    year
    
from df
where year != 2022
group by year
order by year asc
'''

profits_by_year = sql(query)

x = profits_by_year.Year
y = np.cumsum(profits_by_year.Profit)

plt.rcParams["figure.figsize"] = [15, 8]
plt.rcParams["figure.autolayout"] = True
plt.plot(x,y)
plt.xlabel('Year', size = 16)
plt.ylabel('Profit(in Millions)', size = 16)
plt.title('Cummulative Profit', size = 20)
plt.show()

'''
Q5 — From which counties do most of the customers come from
'''
query = '''
select 
    count(distinct customer_name) as Number_of_customers, 
    customer_country
    
from df
group by customer_country
order by customer_country asc
'''

customers_by_country = sql(query)

# Filtering the top ten percentile of countries
top_ten_percentile = top_ten_percentile.sort_values(by = 'Number_of_customers', ascending=False)

print(top_ten_percentile)

sns.barplot(data =top_ten_percentile, x='Number_of_customers', y='customer_country')
plt.show()



