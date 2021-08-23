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

#os.chdir("/Users/matt/Documents/CompSci/GMTK Analysis")

links = pd.read_csv("links2021.csv")

links = np.array(links.iloc[:, 1])
driver = webdriver.Chrome("chromedriver")

pagesToScrape =  2000
startPage = 30

comments = []
madeMusics = []
madeArts = []
ratingsNumbers = []
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


    # for element in content:
    #     print(element.text)

    # description = None
    # mydivs = soup.find_all("dd")
    # if mydivs is not None:
    #     for div in mydivs:               
    #         soup = BeautifulSoup(description)
    #         print(soup.get_text())
    # else:
    #     description = None
    #     print(description)



#         data = []
#         table = soup.find('div', attrs={'class':'game_info_panel_widget'})
#         print(table)
#         if table is not None:
#             table_body = table.find('tbody')

#             rows = table_body.find_all('tr')
#             for row in rows:
#                 cols = row.find_all('td')
#                 cols = [ele.text.strip() for ele in cols]
#                 data.append([ele for ele in cols if ele]) # Get rid of empty values
#             print(data)

#             status = None
#             platforms = None
#             genre = None
#             tags = None
#             publishDate = None
#             author = None

            
#             for row in data:
#                 if (row[0] == "Published"):
#                     publishDate = row[1]
#                 if (row[0] == "Status"):
#                     status = row[1]
#                 if (row[0] == "Author"):
#                     author = row[1]
#                 if (row[0] == "Genre"):
#                     genre = row[1]
#                 if (row[0] == "Tags"):
#                     tags = row[1]
#                 if (row[0] == "Platforms"):
#                     platforms = row[1]
#     except:
#         pass
#     # status = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/a").text
#     # platforms = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/a").text
#     # genre = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/table/tbody/tr[5]/td[2]/a").text
#     # tags = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/table/tbody/tr[6]/td[2]").text


#     #     status = None
#     #     platforms = None
#     #     genre = None
#     #     tags = None



#     #location.send_keys(Keys.COMMAND + 't') 

#     #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 


#     # driver.switch_to.window(driver.window_handles[1])

#     #driver.get("http://stackoverflow.com")

#     # /html/body/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/a
#     # /html/body/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/a
#     # /html/body/div[2]/div[2]/div/div[2]/div[2]/div/div/div[4]/div[1]/a

#     # print(price)
    
#     # print(description)
    
 
#     Rows.append((title,reviews,madeArt,madeMusic, numRatings, noComments, description, status, platforms, genre, tags, author, publishDate))
#     df = pd.DataFrame(Rows,columns=['Title','reviews','madeArt','madeMusic', 'numRatings', "noComments", "description", "status", "platforms", "genre", "tags", "author", "Published" ])
#     df.to_csv('output2021 1-3000 .csv')
# #Links = list(dict.fromkeys(Links)) 
