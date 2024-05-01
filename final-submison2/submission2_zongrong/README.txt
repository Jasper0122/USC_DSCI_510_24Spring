
# Yelp Data Scraper

## Overview
This script allows you to scrape restaurant data from Yelp for a specified location, in this case, Los Angeles. It retrieves details such as the name, location, price, and ratings of restaurants in the high-price range (3 to 4 dollar signs).

## Requirements
- Python 3.x
- `requests` library (Install using `pip install requests`)

## Features
- Scrape a specified number of restaurant entries from Yelp.
- Save the scraped data to a CSV file.

## How to Use

### Setting Up Your Environment
1. Ensure Python 3.x is installed on your system.
2. Install the `requests` library if not already installed.

### Running the Script
1. Obtain a Yelp API Key and replace the `API_KEY` variable's value in the script with your key.
2. Use command-line arguments to control the script's behavior:
   - `--scrape N`: Scrapes the first N entries from Yelp.
   - `--save FILE_PATH`: Saves the scraped data to the specified file path.

### Examples
- To scrape the first 100 restaurant entries:
  ```
  python scraper.py --scrape 100
  ```
- To scrape and save the first 50 restaurant entries to `data.csv`:
  ```
  python scraper.py --scrape 50 --save data.csv
  ```

## Notes
- The script is preset to search for restaurants in Los Angeles within the price range of 3 to 4 dollar signs.
- Ensure you comply with Yelp's API usage policies when using this script.
