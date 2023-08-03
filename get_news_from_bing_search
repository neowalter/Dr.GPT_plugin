
import requests
import pandas as pd
from bs4 import BeautifulSoup
# send a GET request to the source URL
url = "https://www.bing.com/news/search?q=finance&FORM=HDRSC6"
response = requests.get(url)
# check if the request was successful
if response.status_code == 200:
    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # create empty lists to store the news information
    titles = []
    dates = []
    links = []
    
    # find all the div elements that have the class "news-card newsitem cardcommon"
    divs = soup.find_all("div", class_="news-card newsitem cardcommon")
    
    # loop through the div elements
    for div in divs:
        # find the a element that has the class "title" and get its text and href attributes
        a = div.find("a", class_="title")
        title = a.text
        link = a["href"]
        
        # find the span element that has the attribute "aria-label" and get its text
        span = div.find("span", attrs={"aria-label": True})
        date = span.text
        
        # append the information to the lists
        titles.append(title)
        dates.append(date)
        links.append(link)
    
    # create a dataframe from the lists using pandas
    df = pd.DataFrame({"title": titles, "date": dates, "link": links})
    
    # display the dataframe
    print(df)
else:
    # print an error message if the request failed
    print("The request failed with status code:", response.status_code)
