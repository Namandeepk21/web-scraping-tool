import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Define the Amazon search URL (Change the URL based on your location)
URL = "https://www.amazon.com/s?k=wireless+earbuds"

# Set headers to make the request look like it's coming from a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Send the HTTP request
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

# Lists to store scraped data
products = []
prices = []
ratings = []

# Extract product details
for item in soup.find_all("div", class_="s-main-slot s-result-list s-search-results sg-row"):
    for product in item.find_all("div", class_="s-result-item"):
        # Extract product name
        name = product.find("span", class_="a-size-medium")
        if name:
            products.append(name.text.strip())
        else:
            products.append("N/A")

        # Extract product price
        price = product.find("span", class_="a-price-whole")
        if price:
            prices.append(price.text.strip())
        else:
            prices.append("N/A")

        # Extract product rating
        rating = product.find("span", class_="a-icon-alt")
        if rating:
            ratings.append(rating.text.strip())
        else:
            ratings.append("N/A")

    # To prevent getting blocked by Amazon, add a delay
    time.sleep(2)

# Create a Pandas DataFrame
df = pd.DataFrame({"Product Name": products, "Price": prices, "Rating": ratings})

# Save the data to a CSV file
df.to_csv("amazon_products.csv", index=False)

print("Scraping completed! Data saved to amazon_products.csv")