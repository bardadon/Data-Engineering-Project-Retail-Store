'''
Connecting to MySQL
'''
# Connecting to MySQL schema: whiskey_retail_shop
connection = pymysql.connect(host ='localhost',
                             port=int(3306),
                             user='root',passwd=****,db='dwh_whiskey')
# Creating a Cursor object
cursor = connection.cursor()

'''
Generating the date Dimension
'''

# Create dates
start_date = pd.to_datetime('1990-01-01').date()
end_date = pd.to_datetime('2100-01-01').date()

# Get all the dates from 1990-01-01 to 2100-01-01
dates = pd.date_range(start=start_date, end=end_date)

# Insert into a dataframe
dates_df = pd.DataFrame(dates, columns=['Date'])

# Date Key Column
dates_df['Date_key'] = 1000 * dates_df.Date.dt.year + 100 * dates_df.Date.dt.month + dates_df.Date.dt.day

# Day_name Column
dates_df['Day_name'] = dates.day_name()

# Month Column
month_dict = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',
             5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',
             11:'Nov',12:'Dec'}
dates_df['Month'] = dates_df.Date.dt.month
dates_df.Month.replace(month_dict,inplace=True)

# Year Column
dates_df['Year'] = dates_df.Date.dt.year

# Confirm that the Date_key column is unique
assert len(dates_df.Date_key.unique()) == len(dates_df.Date)

'''
Loading the Date Dimension to MySQL
'''
query = '''
drop table if exists dwh_date;
'''

cursor.execute(query)

query = '''
CREATE TABLE dwh_date (
    Date_key INT NOT NULL PRIMARY KEY,
    Dates DATE NOT NULL,
    Day_name VARCHAR(50) NOT NULL,
    Month_name VARCHAR(50) NOT NULL,
    Year_name VARCHAR(50) NOT NULL
);
'''

cursor.execute(query)

# Convert the Dataframe into a list of arrays
records = dates_df.to_records(index=False)

# Convert the list of arrays into a tuple of tuples
result = tuple(records)

for data in range(0,len(result)):
    
    # Create a new record
    query = '''
    insert into dwh_date (Date_key, Dates, Day_name, Month_name, Year_name) values {}
    '''.format(result[data])
    
    
    # Execute the query
    cursor.execute(query)
    
    
# Commit the transaction
connection.commit()
