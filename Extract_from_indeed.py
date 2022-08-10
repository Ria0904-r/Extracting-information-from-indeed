import pandas as pd #pandas is best for handling data
import requests #HTTP requests using Python
import bs4 #Beautiful Soup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup
import re #regular expression
import seaborn as sns #data visualization library based on matplotlib.
global description #defined description globally to use anywhere in the code 

URL1 = "https://in.indeed.com/jobs?q=intern&l=India" #getting link

def parse1(url1): #parsing the html file
    html = requests.get(url1)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
    desc = soup.select(".jobsearch-jobDescriptionText")
    return desc

def parse(url): #parsing and putting the desired objects in the following categories i.e. title, titlelength, loc etc
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
    df = pd.DataFrame(columns=["Title","TitleLength", "Location","Company", "LinkToApply", "Description"])
    
    for each in soup.find_all(class_= "result" ): #for every line in html parsing and putting the values in desired column using try and except
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

        df = df.append({'Title':title, 'Location':location, 'Company':company, 'TitleLength':length, 'LinkToApply':link, 'Description':description}, ignore_index=True) #appending the list and return dataset 
    return df

url2 = "https://in.indeed.com/viewjob?jk=5b624c45642c86fc&tk=1fhnrpvhptv1e801&from=serp&vjs=3" #parsing another link
def parse2(url):
    html = requests.get(url) # getting url
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8").0 # parsing html file using htmlparser
    df = pd.DataFrame(columns=["Title"])

    for each1 in soup.find_all(class_= "result" ):
        try: 
            parse1.description = each1.find(class_='jobsearch-jobDescriptionText').text.replace('\n', '') #it will return the description
        except:
            parse1.description = 'None'
parse2(url2)

parse2(url2)

parse(URL1)
