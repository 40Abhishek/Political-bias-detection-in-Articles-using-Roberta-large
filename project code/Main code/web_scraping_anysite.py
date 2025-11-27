import requests
from bs4 import BeautifulSoup
    
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



prefs = {
    "profile.default_content_setting_values.images": 2,      # 2 = block
    "profile.default_content_setting_values.stylesheets": 2, # block CSS
    "profile.default_content_setting_values.media_stream": 2,# block video/audio
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_setting_values.plugins": 2,
    "profile.default_content_setting_values.popups": 2,
    "profile.managed_default_content_settings.javascript": 2
}


options = Options()
options.add_argument("--inprivate")  
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3")


options.add_experimental_option("prefs", prefs)

driver = webdriver.Edge(service=Service(), options=options)

unit=110


def get_soup(url):
    try:
        print(f"🍲 Scraping: Soup")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Get the page title
        title = soup.find("h1").get_text(strip=True)
        # print("✅ Page Title:", title)

        # Get all paragraphs
        paragraphs =''
        paras=soup.find_all("p")
        for p in paras:
            if (len(p.get_text(strip=True))>unit):
                paragraphs+=p.get_text(strip=True)
        # print("✅ Paragraphs:", paragraphs)

        return title, paragraphs

    except Exception as e:
        print(f"❌ Error:  Using selenium now") #{e}
        # return e
        #when error seen go to get_sel

        return get_sel(url)



def get_sel(url):
    
    driver.delete_all_cookies()
    time.sleep(0.5)
    # url = ""
    driver.get(url)
    print(f"🕷️ Scraping: Sel")
    time.sleep(0.5)

    try:
        # Extract title
        title = driver.find_element(By.TAG_NAME, "h1").text
        # print("✅ Title:", title)

        paragraphs=''
        para = driver.find_elements(By.TAG_NAME, "p")
        for p in para:
            if(len(p.text)>unit):
                if "tribune" in p.text.lower():
                    break

                # Rule 2: ignore 'about us' blocks
                if "copyright" in p.text.lower():
                    break
                
                if "all rights reserved" in p.text.lower():
                    break

                else:
                    paragraphs+=p.text

        # print(f"Paragraph: {paragraphs} \n\n")

    

        return title, paragraphs
    except:
        print("error")
        return '', ''


def main():
    f1=open("scrape_main_data.txt",'r')

    f2=open("article_data.txt",'a',encoding="utf-8")
    
    data=f1.readlines()

    articles=[]

    n=9099
    
    for i in range(8337,n):
        print(f'{i}')
        
        link=data[i].split(sep="@")[3]
        article=data[i].split(sep="@")[1]
        if 'united24media' in article or 'The Voice' in article or 'Patriot Light' in article or 'The Blade' in article:
            f2.write(str(i)+'@@'+'\n')
            print('skip')
            continue
        print(link)
        time.sleep(0.2)
        title, paragraphs=get_soup(link)

        # print(title) #title is a str
        # print(paragraphs) #paragraph is a list of str
        # exit()

        #adding data to .txt
        f2.write(str(i)+'@'+title+'@'+paragraphs+'\n')

    print("====END====\n\n")



if __name__=="__main__":
    main()
    driver.quit()