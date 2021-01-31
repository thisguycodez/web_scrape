from urllib.request import urlopen
from bs4 import BeautifulSoup
from mechanize import Browser



# get the url page to scrape
url_2_scrape = "https://www.amazon.com/s?k=shoes+for+men&crid=38H5KG61ITBPE&sprefix=shoes%2Caps%2C156&ref=nb_sb_ss_ts-a-p_4_5"



# declare browser
br = Browser()

# disable the handle robots method
br.set_handle_robots(False)

# add headers 
br.addheaders = [('Referer', 'https://www.amazon.com'), ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# open browser emulator
br.open(url_2_scrape)

# parse the html response
html = BeautifulSoup(br.response().read(), 'html.parser')



# list of all main tags to loop thorugh  a-section
list_tags = html.find_all('div', class_="a-section")



# file to save it in
items_file = 'items.csv'
file = open(items_file, 'w')
headers = 'item, price \n'
file.write(headers)



# loop through cards to find title and price
for tag in list_tags:
	# from here is where the magic happens


# span tag -(item) a-size-base-plus
	item = tag.find('span', class_="a-size-base-plus")

# span tag -(price) a-price
	price = tag.find('span', class_="a-price")

	cur_line = f"{item}, {price}"
	print(cur_line)

	file.write(cur_line)



file.close()







