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

import bs4
from selenium.webdriver.common.keys import Keys
def extract_stats_data(driver):
    data_div = driver.find_element_by_id('datagrid')
    data_html = data_div.get_attribute('innerHTML')
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

#question 1
team_click = driver.find_element_by_id('st_parent')
team_click.click()

seasontype_click = driver.find_element_by_id('st_hitting_game_type')
seasontype_selcet=Select(seasontype_click)
seasontype_selcet.select_by_visible_text('Regular Season')


data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')

team_2015 = extract_stats_data(data_html)
team_2015

Team_Name = team_2015.iloc[team_2015['HR'].astype('int64').idxmax()]['Team']
print('Answer of Q1 "Which team had the most homeruns in the regular season of 2015?" is ',Team_Name)
#the answer to "Which team had the most homeruns in the regular season of 2015?" is  Toronto Blue Jays


#Question 2
#a
AL = team_2015[team_2015["League"]=="AL"]['HR'].astype('int64').mean()
NL = team_2015[team_2015["League"]=="NL"]['HR'].astype('int64').mean()
if AL>NL:
    print("AL League higher for average number of homeruns be", AL)
else:
    print("NL League higher for average number of homeruns be", NL)
#AL League higher for average number of homeruns be 182.5

#b
split_click = driver.find_element_by_id('st_hitting_hitting_splits')
split_selcet=Select(split_click)
split_selcet.select_by_visible_text('First Inning')

first_inning_2015 = extract_stats_data(data_html)
AL = first_inning_2015[first_inning_2015["League"]=="AL"]['HR'].astype('int64').mean()
NL = first_inning_2015[first_inning_2015["League"]=="NL"]['HR'].astype('int64').mean()
if AL>NL:
    print("AL is higher. Its average number of homeruns is", AL)
else:
    print("NL is higher,Its average number of homerun is", NL)
