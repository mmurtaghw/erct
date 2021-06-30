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


driver = webdriver.Chrome("/home/matt/Documents/gmtkanalysis/chromedriver")


pagesToScrape =  5
startPage = 1

comments = []
madeMusics = []
madeArts = []
ratingsNumbers = []
titles = []
Rows = []

url = ("https://ridie.3ieimpact.org/index.php?r=search/detailView&id=1054")
driver.get(url)