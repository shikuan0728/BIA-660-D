from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import time
import pandas as pd


driver = webdriver.Chrome(executable_path='Users/alienware/Documents/2018Spring/BIA660-D/chromedriver')
driver.get('http://www.mlb.com/')

stats_header_bar = driver.find_element_by_class_name('megamenu-navbar-overflow__menu-item--stats')
stats_header_bar.click()
stats_line_items = stats_header_bar.find_elements_by_tag_name('li')
stats_line_items[0].click()

wait = WebDriverWait(driver, 10)

hitting_season_element = driver.find_element_by_id('st_hitting_season')
season_select = Select(hitting_season_element)

season_select.select_by_value('2015')


def extract_stats_data(driver):
    soup = bs4.BeasutifulSoup(data_html, "html5lib")
    soup.thead
    for t in soup.thead.findAll('th'):
        t.replace('▲', '').replace('▼', '')
        row_head.append(t.text)
        random_delay()
    soup.tbody
    for t in soup.tbody:
        row = soup.t.body.tr.findAll('td')
        t.replace('▲', '').replace('▼', '')
        row_list.append(t.text)
        random.delay()
    data = pd.DataFrame(row_data, columns=row_head)
    pass

team_hr_stats = wait.until(EC.visibility_of_element_located((By.ID, 'datagrid')))

