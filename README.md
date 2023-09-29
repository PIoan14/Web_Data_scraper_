# Web_Data_scraper_
Scraping Bot which can be controlled from a it's web interface

# Built using VS Code
# Usability
Inside the web interface, you can pass in as many domains as you wish. Then, you should check the boxes coresponding with
the data you are looking for (you can choose between Entity name, Email or Phone Number). The app will than search for all the elements 
from all the web pages you've passed in. If the element is not found on a specific page, it will be replaced with <<['no element']>> string.
Make sure you introduce valid URLs, otherwise, no data will be returned. Also, all the 'no URL' format is automatically eliminated from the sent request. 
Finally, after the processing faze, the data will be shown in the output box and it will also be downloadable into a csv document format.

# Requirements
-VS Code (HTML, CSS and Python extension, Python 3)
-The following python libraries should be installed : flask, spacy, re , pandas, flask_cors, bs4 (BeautifulSoup), requests. 
-After you've installed python and VS Code you can use 'pip install <lipbrary_name>' in you computer's terminal in order to get the needed libraries.
exepmle : pip install pandas

# Some usefull information can also be found on the web page itself...
# THANK YOU


