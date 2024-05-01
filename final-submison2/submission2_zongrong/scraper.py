import requests
import csv
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--scrape', type=int, help='Scrape the first N entries')
parser.add_argument('--save', type=str, help='Save the scraped data to the file path')
args = parser.parse_args()

# Yelp API Key
API_KEY = 'NFPWCChl94oCIGYBJJWC_HBRNLxCVzrVxl_U0UZSAKJC3ghcrNlcxuGkG5RkPSlfXaZOS09psuwDqCSHKLL5UE7_OJCqb7iOnmX8LhZgZuO0AknoxNVwxq9jlWIYZnYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer {}'.format(API_KEY)}

# Function to scrape data from Yelp
def scrape_data(scrape_limit=None):
    PARAMETERS = {
        'term': 'restaurants',
        'limit': 50 if not scrape_limit else scrape_limit,
        'location': 'Los Angeles',
        'offset': 0
    }

    businesses = []

    while True:
        response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)
        data = response.json()

        # Check if data is available
        if 'businesses' in data and len(data['businesses']) > 0:
            for business in data['businesses']:
                # If a scrape limit is set and we've reached it, break out of the loop
                if scrape_limit and len(businesses) >= scrape_limit:
                    break
                # Otherwise, add the business to our list
                businesses.append(business)
            # If we've reached the scrape limit, stop requesting more data
            if scrape_limit and len(businesses) >= scrape_limit:
                break
            PARAMETERS['offset'] += PARAMETERS['limit']
        else:
            break

    # Extract only the required fields
    businesses = [{
        'ID': business['id'],
        'latitude': business['coordinates']['latitude'],
        'longitude': business['coordinates']['longitude'],
        'NAME': business['name'],
        'Review_num': business['review_count'],
        'Rating': business['rating'],
        'Categories': ', '.join([category['title'] for category in business['categories']]),
        'Price': business.get('price', '')
    } for business in businesses]

    return businesses

# Function to save data to a CSV file
def save_to_csv(businesses, file_path):
    fieldnames = ['ID', 'latitude', 'longitude', 'NAME', 'Review_num', 'Rating', 'Categories', 'Price']
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(businesses)

# Main execution logic
if __name__ == '__main__':
    # Scrape the data
    businesses = scrape_data(scrape_limit=args.scrape if args.scrape else None)

    # If a save path is provided, save the data to a CSV
    if args.save:
        save_to_csv(businesses, args.save)
    # Otherwise, print the data
    else:
        for business in businesses:
            print(business)
