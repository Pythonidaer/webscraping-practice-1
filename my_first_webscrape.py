from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphics+cards'

# open connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# page_soup.h1

# grabs each product
cells = page_soup.findAll("div", {"class":"item-cell"})

# create a file called products.csv and allow it to be written into
filename = "products.csv"
f = open(filename, "w")

# write field headers into the data
headers = "product_name, shipping\n"
f.write(headers)

for cell in cells:
    # Get the brand of the Product
    # brand = cell.div.div.div.a.img["title"]

    # Get the Product itself and its link
    item_title = cell.findAll("a",{"class":"item-title"})
    product_name =  item_title[0].text

    # Get the Product shipping information
    shipping_list = cell.findAll("li",{"class":"price-ship"})
    shipping = shipping_list[0].text.strip()

    # print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(product_name.replace(",", "|") + "," + shipping + "\n")

f.close()