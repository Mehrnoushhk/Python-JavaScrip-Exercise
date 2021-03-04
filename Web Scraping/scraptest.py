from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


try:
    html = urlopen('http://pythonscraping.com/pages/page1254.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('Check the URL')
else:
    print('Anyway...')




bs = BeautifulSoup(html, 'html.parser')

print(bs.h1)