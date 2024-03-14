import pandas as pd
from selenium import webdriver
from io import StringIO


"""Specifically for NC schools this useful database exists: http://apps.schools.nc.gov/ords/f?p=125:1:::NO:::
Scraping tutorial: https://medium.com/nerd-for-tech/web-scraping-beautiful-soup-and-selenium-468ed6e0dbef"""

url = "https://www.greatschools.org/north-carolina/schools/?view=table&gradeLevels=h"

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source

table = pd.read_html(StringIO(str(html)))

print(table)
