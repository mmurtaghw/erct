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
import numpy as np
from webdriver_manager.chrome import ChromeDriverManager

#os.chdir("/Users/matt/Documents/CompSci/GMTK Analysis")

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('incognito')
options.add_argument("user-data-dir=/Users/matt/Library/Application Support/Google/Chrome/Default")
# options.add_experimental_option('prefs', {
# "download.default_directory": dir, #Change default directory for downloads
# "download.prompt_for_download": False, #To auto download the file
# "download.directory_upgrade": True,
# "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
# })

#/Users/matt/Library/Application Support/Google/Chrome/Default
driver= None
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options, port = 5102)
/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a
/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span

url = ("https://www.amazon.co.uk/s?rh=n%3A349779011&fs=true&ref=lp_349779011_sar")
driver.get(url)


# for i in range(startPage,pagesToScrape):
    
#     pageNumber = str(i)
 
#     url = ("https://ridie.3ieimpact.org/index.php?r=search/detailView&id=" + str(i))
#     driver.get(url)
#     print(i)


#     driver.get(url)


#     reviews = ""
#     skip = False
#     headings = driver.find_elements_by_css_selector("dt")
#     contents = driver.find_elements_by_css_selector("dd")

#     colnames = []
#     colcont = []
#     for heading, content in zip(headings, contents):

#             colnames.append(heading.text)
#             colcont.append(content.text)

#     colcont = np.array(colcont)
#     colnames = np.array(colnames)
#     print(len(colnames))
#     print(len(colcont))

#     if i == 30:
#         output = pd.DataFrame(colcont.transpose())
#         output = output.transpose()
#         output.columns = colnames
#         output = output.astype(str)
#         print(output)
#     else:
#         df = pd.DataFrame(colcont)
#         if df.empty:
#             continue
#         j += 1
#         print(len(colnames))
#         print(len(output.loc[0]))

#         df = df.transpose()
#         df.index = [i]
#         df.columns = colnames
#         df = df.astype(str)
#         print(df)
#         print(output)
#         df.to_csv("RIDIE" + str(i) + ".csv")
#         #output = pd.concat([df, output], axis=0, sort = False, join="inner")        
