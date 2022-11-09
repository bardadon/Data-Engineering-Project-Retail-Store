# Data-Engineering-Project-Retail-Store
In this project, I created an entire data architecture for a made-up whiskey retail shop that will enable shop managers to make decisions based on their data. 
This project will simulate the entire process that data-driven companies do to make data-based decisions.
The project will include Web Scraping, processing and transforming data, loading and designing a Database and a Data Warehouse, and finally, analysis and descision making. 

Check out my series of articles illustrating in details how I created the project.

Part 1 - https://medium.com/towardsdev/data-engineering-project-retail-store-part-1-web-scraping-a99ac5d6d44c

Part 2 - https://towardsdev.com/data-engineering-project-retail-store-part-2-loading-the-data-7c15c9c387e4

Part 3 - https://towardsdev.com/data-engineering-project-retail-store-part-3-data-warehousing-519b74a0b6c4

Part 4 - https://medium.com/codex/data-engineering-project-retail-store-part-4-analyzing-the-data-630efad6e09a

## Project Architecture


## Part 1 - Web Scraping
Run this to apply the code:

```
# Import the whisky_web_scraping class
from Helper import whisky_web_scraping

# Create a scraper object
scraper = whisky_web_scraping()

# Scrape Data
data = scraper.scrape_whisky(number_of_pages=5)
```

### End Result

1. Panda's DataFrame with product data:
```
|    |Product_Name                                     |Alcohol_Percent  |Alcohol_Amount|Alcohol_Price|
|----|-------------------------------------------------|-----------------|--------------|-------------|
|0   | Deanston 18 Year Old                            |46.3             |70           |63.95        |
|1   |Lagavulin 2006 Distillers Edition                |43               |70            |89.95        |
|2   |Benromach Cask Strength Vintage 2010             |58.5             |70            |51.95        |
|3   |Personalised Highland Special Reserve Single Malt|48               |70            |54.95        |
|4   |Blair Athol 12 Year Old                          |43               |70            |48.45        |
|    |...                                              |...              |...           |...          |
|4441|Amrut Indian Single Malt Whisky Tasting Set      |49.6             |18            |44.95        |
|4442|Paul John Mithuna Sample                         |58               |3             |15.95        |
|4443|Milk & Honey Peated Cask Sample                  |46               |3             |5.75         |
|4444|Kavalan Bourbon Oak Sample                       |46               |3             |7.75         |
|4445|Kavalan Sherry Oak Sample                        |46               |3             |8.75         |
```

2. Exported CSV files of each type of Whisky:
![1 Vs11yEJxOI_Hv7D-stA-JA](https://user-images.githubusercontent.com/65648983/200838844-72029ee7-eca8-4f19-a0f9-1a54ce43d1e3.png)

## Part 2 - Loading the Data and Designing a Database


## part 3 - Designing a Data Warehouse


## Part 4 - Analyzing the Data
