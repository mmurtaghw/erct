from typing import Container
from numpy.core.fromnumeric import transpose
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import re
from bs4 import BeautifulSoup
import numpy as np


links = pd.read_csv("links2021.csv")

links = np.array(links.iloc[:, 1])
driver = webdriver.Chrome("chromedriver")

pagesToScrape =  2000
startPage = 30

titles = []
Rows = []
j = 0

for i in range(startPage,pagesToScrape):
    
    
    pageNumber = str(i)
 
    url = ("https://ridie.3ieimpact.org/index.php?r=search/detailView&id=" + str(i))
    driver.get(url)
    print(i)
    


    driver.get(url)

    #print(url)

    # price = driver.find_element_by_class_name("Price").text

    # Prices.append(price)

    
    #location = location.get_attribute('href')

    # Locations.append(location)
    
    # description = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/div[6]").text

    # Descriptions.append(description)
    
    # date = driver.find_element_by_class_name("Posted_date").text
    
    # title = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/span[2]/span[1]").text

    #/html/body/div[2]/div[3]/div/div[2]/section[5]/div/div[2]/div[1]/div[2]/div[2]/div[1]
    #/html/body/div[2]/div[3]/div/div[2]/section[5]/div/div[2]/div[2]/div/div[2]/div[1]
    #/html/body/div[2]/div[3]/div/div[2]/section[5]/div/div[2]/div[3]/div/div[2]/div[1]



    reviews = ""
    skip = False
    headings = driver.find_elements_by_css_selector("dt")
    contents = driver.find_elements_by_css_selector("dd")

    colnames = []
    colcont = []
    for heading, content in zip(headings, contents):

            colnames.append(heading.text)
            colcont.append(content.text)

    colcont = np.array(colcont)
    colnames = np.array(colnames)
    print(len(colnames))
    print(len(colcont))

    if i == 30:
        output = pd.DataFrame(colcont.transpose())
        output = output.transpose()
        output.columns = colnames
        output = output.astype(str)
        print(output)
    else:
        df = pd.DataFrame(colcont)
        if df.empty:
            continue
        j += 1
        print(len(colnames))
        print(len(output.loc[0]))

        df = df.transpose()
        df.index = [i]
        df.columns = colnames
        df = df.astype(str)
        print(df)
        print(output)
        df.to_csv("RIDIE" + str(i) + ".csv")
        #output = pd.concat([df, output], axis=0, sort = False, join="inner")        
