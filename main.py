from bs4 import BeautifulSoup
import requests
from csv import writer

# add url
url = "url"
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

# add html tags from website example: find_all('div' and class_='container')
lists = soup.find_all('htmltag',class_="class name")

# create file 
with open('example.csv','w',encoding='utf8',newline='') as f:
  thewriter = writer(f) 
  header = ['title','description']
  thewriter.writerow(header)


  for item in lists:
    title = item.find('htmltag',class_="class name").text().replace('\n','')

    data = [title]
    thewriter.writerow(data)




