import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

class whisky_web_scraping():
    
    def scrape_html(self,base_url, page):
        '''
        Sending a GET request to https://www.thewhiskyexchange.com/ and creating a Beautiful Soup object.
        
        Args:
            base_url(String)              
            page(Int) - Which page to scrape.
            
        Returns
            soup(BeautfulSoup Object)         
        '''
        
        self.base_url = base_url
        self.page = page

        url = base_url + str(page)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        return soup
    
    def get_page_content(self, soup):
        '''
        Extract from soup all the html object of type div and of class product-card__content.
        
        Args:
            soup(BeatifulSoup Object)
            
        Returns:
            proudcts_info_content(List of html objects) - List of div objects that contain the name of the beverage, the alcohol amount and percent.
        
        '''
        self.soup = soup
        
        proudcts_info_content = soup.find_all('div', class_ = 'product-card__content')
        return proudcts_info_content
        
    
    def get_page_price(self, soup):
        '''
        Extract from soup all the html object of type div and of class product-card__data.
        
        Args:
            soup(BeatifulSoup Object)
            
        Returns:
            proudcts_info_data(List of html objects) - List of div objects that contain the price of the beverage.
        
        '''
        self.soup = soup

        proudcts_info_price = soup.find_all('div', class_ = 'product-card__data')
        return proudcts_info_price

    
    def get_product_name(self, proudcts_info_content):
        '''
        Extract the name of product.
        
        Args:
            proudcts_info_content(String) - The div object of class product-card__content.
        
        Returns:
            product_name(List) - A list of names.
        '''
        
        self.proudcts_info_content = proudcts_info_content        
    
        product_name = []
        
        # Iterate through each product in the webpage 
        for product in range(len(proudcts_info_content)):
            
            # Extract the first class P - Which holds the name of the beverage
            name_p = proudcts_info_content[product].find_all('p')[0]
            
            # Extract the contents of the first paragraphs - the name of the beverage       
            alcohol_name = name_p.contents[0].strip()
            
            # Append each name to the list
            product_name.append(alcohol_name)
            
        return product_name

    def get_product_alcohol_percent(self, proudcts_info_content):
        '''
        Extract the alcohol percent of product.
        
        Args:
            proudcts_info_content(String) - The div object of class product-card__content.
        
        Returns:
            product_al_percent(List) - A list of alcohol percent.
        '''
        
        self.proudcts_info_content = proudcts_info_content        
    
        product_al_percent = []
        
        # Iterate through each product in the webpage 
        for product in range(len(proudcts_info_content)):
            
            # Extract the second class P - Which holds the alcohol values
            al_p = proudcts_info_content[product].find_all('p')[1]
            
            # Apply string manupulation to extract the alcohol percent
            alcohol_percent_str = al_p.contents[0].strip()
            start_location_percent = alcohol_percent_str.find('/ ') 
            end_location_percent = alcohol_percent_str.find('%')
            alcohol_percent = alcohol_percent_str[start_location_percent + 2:end_location_percent]
            
            # Append each alcohol percent to the list
            product_al_percent.append(alcohol_percent)
            
        return product_al_percent
    
    
    def get_product_alcohol_amount(self, proudcts_info_content):
        '''
        Extract the alcohol amount of product.
        
        Args:
            proudcts_info_content(String) - The div object of class product-card__content.
        
        Returns:
            product_al_percent(List) - A list of alcohol amount.
        '''
        self.proudcts_info_content = proudcts_info_content        

        product_al_amount = []
        
        # Iterate through each product in the webpage 
        for product in range(len(proudcts_info_content)):
            
            # Extract the second class P - Which holds the alcohol values
            al_p = proudcts_info_content[product].find_all('p')[1]
            
            # Apply string manupulation to extract the alcohol amount
            alcohol_percent_str = al_p.contents[0].strip()
            start_location_amount = 0
            end_location_amount = alcohol_percent_str.find('cl')
            alcohol_amount = alcohol_percent_str[start_location_amount:end_location_amount]
            
            # Append each alcohol amount to the list
            product_al_amount.append(alcohol_amount)
            
        return product_al_amount
    
    def get_product_price(self, proudcts_info_price):
        '''
        Extract the price of product.
        
        Args:
            proudcts_info_content(String) - The div object of class product-card__data.
        
        Returns:
            product_price(List) - A list of prices.
        '''
        self.proudcts_info_price = proudcts_info_price
    
        product_price = []
        
        # Iterate through each product in the webpage 
        for product in range(len(proudcts_info_price)):
            
            # Extract the price for each product 
            alcohol_price = proudcts_info_price[product].contents[0].contents[0].replace('£','').strip()
            
            # Append each alcohol price to the list
            product_price.append(alcohol_price)
            
        return product_price
    
    def create_df(self, names, alcohol_amount, alcohol_percent, price):
        '''
        Create a DataFrame that will hold the extracted data.
        
        Args:
            names(List) - A list of of product names.  
            alcohol_amount(List) - A list of of product alcohol amounts.  
            alcohol_percent(List) - A list of of product alcohol percent.  
            price(List) - A list of of product prices.  
        
        Returns:
            original_df(DataFrame)
        '''
        
        
        self.names = names
        self.alcohol_amount = alcohol_amount
        self.alcohol_percent = alcohol_percent
        self.price = price
        
        # Create a DataFrame
        original_df = pd.DataFrame(names, columns=['Product_Name'])
        original_df['Alcohol_Percent'] = alcohol_percent
        original_df['Alcohol_Amount'] = alcohol_amount
        original_df['Alcohol_Price'] = price
        
        return original_df
    
    def insert_to_df(self, original_df, new_df):
        '''
        Insert new data into an existing dataframe.
        
        Args:
            original_df(DataFrame) : DataFrame with data from the first page of a product.
            new_df(DataFrame) : DataFrame with data from other pages. 
            
        Returns:
            original_df(DataFrame) : DataFrame with data from original_df + new_df.
        '''
        
        self.original_df = original_df
        self.new_df = new_df
        
        # Insert new data into the DataFrame of the first page
        original_df = original_df.append(new_df,ignore_index=True, verify_integrity = True)

        return original_df
    
    def get_links(self, url = 'https://www.thewhiskyexchange.com/'):
        '''
        Generate a list of links that showcase whiskey beverages.
        
        Args:
            url(String) - The URL of the main page.
                Default - https://www.thewhiskyexchange.com/
        Returns:
            relevant_links(List) - A list of only the links that showcase a type of whiskey.
        '''
        
        self.url = url
        
        # Generate a BeautifullSoup object called soup
        url = url
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        
        # Collect all the html objects of type 'a'
        a_tags = soup.find_all('a', class_ ='subnav__link' )
        
        links_list = []
        
        # Collect all the hyper links of the webpage.
        for link in a_tags:
            links_list.append(link.get('href'))

        relevant_links = []
        
        # Iterate through the links and filter only the relevant ones that showcase a type of whiskey.
        for link in links_list:
            if link is not None and '/c/' in link and 'whisky' in link and '?' not in link:
                relevant_links.append(link)

        return relevant_links

    def scrape_whisky(self, url = 'https://www.thewhiskyexchange.com', number_of_pages = 5):
        '''
        1. Combining all of the methods into a single place. 
        2. Extracting a default number of pages from every page that showcases a type of whiskey.
        3. Export each data of each whiskey type to a CSV file. 
        4. Return a single DataFrame with all of the scraped whiskey data.
        
        Args:
            url(String) - The base url to extract data from.
                Default - https://www.thewhiskyexchange.com
                
						number_of_pages(Int) - The total number of pages to scrape.
							  Default = 5
        
        Returns:
            df(DataFrame) - The entire data scraped throughout this project in a single DataFrame.
        '''
        
        self.url = url
        self.number_of_pages = number_of_pages
        df = pd.DataFrame()
        # Creating a scraper object 
        s = whisky_web_scraping()
        
        # Generating the relevant links to scrape data from
        links = s.get_links()
        
        # Iterating throught each link
        for link in links:
            
            try:
                # For each page in each link, generate a DataFrame of whiskey related data
                for page in range(0,number_of_pages):
                    soup = s.scrape_html(base_url = url + link + '?pg='
                                                    ,page = page+1)

                    content_html = s.get_page_content(soup)
                    price_html = s.get_page_price(soup)

                    names = s.get_product_name(content_html)
                    alcohol_amount = s.get_product_alcohol_amount(content_html)
                    alcohol_percent = s.get_product_alcohol_percent(content_html)
                    price = s.get_product_price(price_html)
                    
                    # Create a new DataFrame for the first page of each whiskey type
                    if page == 0:
                        data = s.create_df(names,alcohol_amount, alcohol_percent, price)
                    
                    # Insert to an existing DataFrame new data.
                    data = s.insert_to_df(data, s.create_df(names,alcohol_amount, alcohol_percent, price))                  
            except:
                print('Error with the link: {}'.format(link))
            # Export data for each whiskey type to a seperate CSV file
            finally:
                start_location = link.rfind('/')+1
                end_location = len(link)
                data.to_csv(link[start_location:end_location] + '.csv')
                df = df.append(data, ignore_index = True)
                
        return df
