

# Created by Sachin Dev on 26/05/18


import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.flipkart.com/omron-hem-8712-bp-monitor/p/itmf3j84uxgkxcff")

#<div class="_1vC4OE _3qQ9m1">₹1,570</div>

content=request.content

soup = BeautifulSoup(content, "html.parser")

element = soup.find("div", {"class":"_1vC4OE _3qQ9m1"})

element=element.text.strip()

s_string = element[1:]

s_string=s_string.replace(",", "")

print (int(s_string))


