import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape
url = "https://fashionunited.com/news/fashion/embracing-comfort-woven-footwear-for-ss24/2024050859770"

# Send a GET request to the URL and retrieve the webpage content
response = requests.get(url)

# Create a BeautifulSoup object by passing the webpage content and specifying the parser
soup = BeautifulSoup(response.content, "html.parser")

# Extract the title
title = soup.find("h1").text

# Extract the article content
content = soup.find("div", class_="css-1s0my6s e15wwp330").get_text(strip=True)

# Display the extracted information
print("Title:", title)
print("Content:", content[:200], "...")  # Display the first 200 characters for preview
