import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time
URL = "https://www.amazon.in/s?k=lip+gloss&crid=1977L0SGS24VY&sprefix=lip+gloss%2Caps%2C330&ref=nb_sb_noss_2"
HEADERS = {
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept-language": "en-US,en;q=0.9",

}
response = requests.get(URL,headers=HEADERS)
soup = BeautifulSoup(response.content,"html.parser")

products=[]
prices=[]
ratings=[]
# for item in soup.find_all("div",class_="s-main-slot s-result-list s-search-results sg-row"):
#     for product in item.find_all("div",class_="s-result-item"):
#         name = product.find("span",class_="a-size-medium")
#         if name:
#             products.append(name.text.strip())
#     else:products.append("N/A")

# price=product.find("span",class_="a-price-whole")
# rating=product.find("span",class_="a-icon-alt")
# if rating:ratings.append(rating.text.strip())
# else:ratings.append("N/A")
# time.sleep(2)

# df.to_csv("amazon_product.csv",index=False)
# print("Scraping completed! Data saved to amazon_products.csv ")


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