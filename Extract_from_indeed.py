import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
import re
import seaborn as sns
global description

URL1 = "https://in.indeed.com/jobs?q=intern&l=India"

def parse1(url1):
    html = requests.get(url1)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
    desc = soup.select(".jobsearch-jobDescriptionText")
    return desc

def parse(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
    df = pd.DataFrame(columns=["Title","TitleLength", "Location","Company", "LinkToApply", "Description"])
    
    for each in soup.find_all(class_= "result" ):
        try: 
            title = each.find(class_='jobTitle').text.replace('\n', '')
        except:
            title = 'None'
        try:
            location = each.find(class_="companyLocation").text.replace('\n', '')
        except:
            location = 'None' 
        try: 
            company = each.find(class_='companyName').text.replace('\n', '')
        except:
            company = 'None'
        try:
            l = each['href']
            link = "https://in.indeed.com" + l
        except:
            link = 'None'

        length = len(title)
      
        description = parse1(link)
        # description.get_text()

        df = df.append({'Title':title, 'Location':location, 'Company':company, 'TitleLength':length, 'LinkToApply':link, 'Description':description}, ignore_index=True)
    return df

url2 = "https://in.indeed.com/viewjob?jk=5b624c45642c86fc&tk=1fhnrpvhptv1e801&from=serp&vjs=3"
def parse2(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8").0
    df = pd.DataFrame(columns=["Title"])

    for each1 in soup.find_all(class_= "result" ):
        try: 
            parse1.description = each1.find(class_='jobsearch-jobDescriptionText').text.replace('\n', '')
        except:
            parse1.description = 'None'
parse2(url2)

parse2(url2)

parse(URL1)
