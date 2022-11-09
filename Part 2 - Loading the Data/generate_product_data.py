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
