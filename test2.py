import requests 
from bs4 import BeautifulSoup
import csv
startUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(startUrl)
# print(page)
soup = BeautifulSoup(page.text, "html.parser")
# def scrapedata():
def scrapeData():
    headers = ["Name", "Distance", "Mass", "Radius"]
    stars_data = []
    for tr in soup.find_all("tr"):
        tempList = []
        td_tags = tr.find_all("td")
        for index, td_tag in enumerate(td_tags):
            if (index == 0):
                tempList.append(td_tag.find_all("a"))
                td_tag.strip(",")
            else:
                try:
                    tempList.append(td_tag.contents[0])
                    td_tag.strip(",")
                except:
                    tempList.append("")
        # for index, td_tag in enumerate(td_tags):
        #     if (index ==1):
        #         tempList.append(td_tag.contents[0])
        #     else:
        #         tempList.append("")
        stars_data.append(tempList)
    with open("happy.csv", "w", encoding = "utf-8") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(stars_data)
scrapeData()