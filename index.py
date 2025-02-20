import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time
URL = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
HEADERS = {
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept-language": "en-US,en;q=0.9",

}
response = requests.get(URL,headers=HEADERS)
soup = BeautifulSoup(response.content,"html.parser")

products=[]
prices=[]
ratings=[]


# Extract product details
for product in soup.find_all("div", class_="s-result-item"):
    # Extract product name
    name = product.find("span", class_="a-size-medium")
    products.append(name.text.strip() if name else "N/A")

    # Extract product price
    price = product.find("span", class_="a-price-whole")
    prices.append(price.text.strip() if price else "N/A")

    # Extract product rating
    rating = product.find("span", class_="a-icon-alt")
    ratings.append(rating.text.strip() if rating else "N/A")

# Ensure all lists are the same length
min_length = min(len(products), len(prices), len(ratings))
products = products[:min_length]
prices = prices[:min_length]
ratings = ratings[:min_length]
print(products)
print(prices)
print(ratings)
print(response.status_code)
print(response.text[:1000])
# Create DataFrame
df = pd.DataFrame({"Product Name": products, "Price": prices, "Rating": ratings})
df.to_csv("amazon_products.csv", index=False)

print("Scraping completed! Data saved to amazon_products.csv")