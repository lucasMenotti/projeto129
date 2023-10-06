from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_scraper_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    
    try : 
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content,"html.parser")
        templist = []

        for tr_tag in soup.find_all("tr", attrs={"class":"fact_row"}):
            td_tags = tr_tag.find_all("td")

            for td_tag in td_tags:
                try:
                    templist.append(td_tag.find_all("div", attrs = {"class":"value"})[0].contents[0])
                except : 
                    templist.append("")

        new_scraper_data.append(templist)

    except :
        time.sleep(1)
        scrape_more_data(hyperlink)



stars_df_1 = pd.read_csv("updated_scraped_data.csv")


for index, row in stars_df_1.iterrows():
    
    scrape_more_data(row["hyperlink"])

    print(f"Coleta de dados do hyperlink {index+1} concluída")

print(new_scraper_data)


scraped_data = []

for row in new_scraper_data:
    replaced = []

    for el in row:
        el = el.replace("\n", "")
        replaced.append(el)

    scraped_data.append(replaced)



print(scraped_data)

headers = ["star_type","discovery_date", "mass", "star_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_stars_df_1 = pd.DataFrame(scraped_data,columns = headers)

new_stars_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
