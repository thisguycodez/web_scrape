# web_scrape
python - web scraping with python,beautiful soup, and mechanize. Getting started Tutorial.



            *********STEPS *********
/////////////////////////////////
step 1: 
   install beautiful soup(bs4) and mechanize -
~#: pip3 install bs4 mechanize html2text

{BeautifulSoup : HTML-Parser}
{Mechanize: Browser Emulator}


/////////////////////////////////
step 2:
  Import everything you will need - 
 
-from urllib.request import urlopen
-from bs4 import BeautifulSoup
-from mechanize import Browser
-from html2text import html2text

/////////////////////////////////
step 3: 
Save the web page you want to scrape it to a variable and declare/start your browser emulator -

-url_2_save = "yoururl.com"

-browser = Browser()


/////////////////////////////////
step 4:
set up the a few things within the browser emulators settings -

-browser.set_handle_robots(False)

{setting this to false will declare that the browser we are emulating is in fact making these movements as human actions and not just following request from a robot.txt file} 

-browsers.addheaders = [('Referer', 'https://www.amazon.com'), ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



/////////////////////////////////
step 5:
   open the browser emulator , parse the page you've requested, and create a list of tags we will be searching through:

-browser.open(url_2_save)

-html = BeautifulSoup(browser.response().read(), 'html.parser')

body = html.find('body', class_="a-m-us")
list_tags = body.find_all('div', class_="a-section")


/////////////////////////////////
step 6:
   As we are scraping we will be writing what we've scrapped into a csv file. When we are done looping, close the file-

items_file = 'items.csv'
file = open(items_file, 'w')
headers = 'item, price \n'
file.write(headers)

-for tag in list_tags:
       # span tag -(item) a-size-base-plus
	item = tag.find('span', class_="a-size-base-plus")

       # span tag -(price) a-price
	price = tag.find('span', class_="a-price")

	cur_line = f"{item}, {price}"
	cur_line = html2text(cur_line)


	# avoiding 'None' values
	if 'None' in cur_line:
		continue
	else:
		print(cur_line)
		file.write(cur_line)



file.close()

/////////////////////////////////


*****CONGRATS YOU GOT A GREAT START ON WEB SCRAPPING*****
*****SEE HOW FAR YOU CAN GO AN SHARE IN THE COMMENTS*****

            *********STEPS *********
