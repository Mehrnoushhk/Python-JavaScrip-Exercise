from bs4 import BeautifulSoup
import requests

# with open('Web Scraping/Home.html', 'r') as html_file:
#     content = html_file.read()
#     my_soup = BeautifulSoup(content, 'lxml')
#     course_cards = my_soup.find_all('div', class_='card')
#     for course in course_cards:
#         print(course.h5.text)
#         print(course.a.text.split()[-1])

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
print(company_name)