# Web Scraping Practice 1
Testing Anaconda, Python and Beautiful Soup. Heck, I just want to see if I can make things work on the first try.

Edit: I made it work!

1. install Anaconda/Python
2. `pip install bs4`
3. open the cmd line > `python` > `import bs4`
4. `from urllib.request import urlopen as uReq`
5. `from bs4 import BeautifulSoup as soup`
6. exit python
7. from command line, `python my_first_webscrape.py`

Watch video below for full instructions. Basically, you get the URL from the place you want to scrape data from. Then, you download the entire HTML website with uReq.

Once you parse the html with beautiful soup, you can begin searching for specific areas. In this tutorial, we searched for item-cells (item-containers in the video), because they were lists of product items and made for a good looping-over tutorial.

Once we find all the information we are looking for, we loop over it. However, There is no safety nets for if information isn't present, so I commented out brand as missing titles lead to syntax errors when no objects were found.

Once we have test logged our data in the console, we create a csv file. Make sure it is writeable before looping data into it. Also, since we are using a comma separated value file, make sure to replace every comma within the file with a pipe `|` symbol or something that isn't a comma. Close the file when complete.

I didn't own a Microsoft Excel license, but I was able to import this into Google Sheets just find!


## Special thanks to Data Science Dojo for this tutorial
[click here to see the YouTube](https://www.youtube.com/watch?v=XQgXKtPSzUI)