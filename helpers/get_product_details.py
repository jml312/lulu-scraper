from requests import get
from bs4 import BeautifulSoup

def get_product_details(url, size_to_check):  
  res = get(url)
  soup = BeautifulSoup(res.content, 'html')
  
  price_text = soup.find("span", class_="price").text.split("\xa0")
  price = price_text[0] if len(price_text) == 2 else price_text[1]
  
  is_available = None
  sizes = soup.find_all("span", class_="sizeTile-bFZ56")
  for size in sizes:
    text = size.text
    data = text.split("\xa0")
    size, availability = data[0], len(data) == 1 
    
    if size == size_to_check.upper():
      is_available = availability
  
  return is_available, price