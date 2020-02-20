Python3.6 and pip3 installation:
$ sudo apt update
$ sudo apt install python3.6
$ python3 -V
$ sudo apt install python3-pip
$ pip3 --version

Virtualenv installation:
$ pip3 install pipenv
$ sudo apt install virtualenv

Virtualenv creation and activation:
$ virtualenv --python=/usr/bin/python3.6 python36
$ source python36/bin/activate


Scrapy installation using pip3:
$ pip3 install scrapy

To show all installed library
$ pip3 freeze


Quotes to Scrape Project

Create new Scrapy project:
$ cd /opt/projects/web-crawler/scrapy-example/amazon-test-crawler 
$ scrapy startproject quotetutorial*

Run the scrapy project
$ scrapy crawl quotes [quotes come from the name of the quotes_spider.py file]


For opening a shell:
$ scrapy shell “http://quotes.toscrape.com/”
>>> response.xpath("//title/text()").extract()
>>> response.xpath("//span[@class='text']/text()").extract()
For index 1
>>> response.xpath("//span[@class='text']/text()")[1].extract()
>>> response.css("li.next a").xpath("@href").extract()
For all href tags
>>> response.css("a").xpath("@href").extract()

Save data into json file
$ scrapy crawl quotes -o items.json

Save data into csv file
$ scrapy crawl quotes -o items.csv

Save data into xml file
$ scrapy crawl quotes -o items.xml

Adding Interpreter:
 
Go to File->Settings->Project Settings->Project Interpreter->Python Interpreters
There will be a "+" sign on the right side. Navigate to your python binary, PyCharm will figure out the rest.


Sqlite opendb:
https://sqliteonline.com/

Opendb-> myquotes.db


MySQL database connection:
For the connection from scrapy to MySQL database required pycharm mysql connector or install the database using pip3.



MongoDB connection from scrapy project:
Step1. Install the mongodb database
Step2. 
Download the debian file from the link: https://www.mongodb.com/download-center/compass
Then open with software install 
 
For MongoDB connector install package from pycharm ‘pymongo’
Or using ‘pip3 install pymongo’

