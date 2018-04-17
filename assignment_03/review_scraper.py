
# coding: utf-8

# In[1]:


import requests
import bs4


# In[2]:


url_1 = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber=1"""


# In[3]:


url_1


# In[4]:


soup_1 = bs4.BeautifulSoup(requests.get(url_1).text, 'html5lib')
review_general_1 = soup_1.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_1 = review_general_1.find_all('div', attrs={'class': 'a-section review'})
review_title_1 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_1]
review_body_1 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_1]
review_stars_1 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_1]
review_date_1 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_1]
review_title_1, review_body_1, review_stars_1, review_date_1


# In[5]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_2 = url+str(2)
url_2


# In[6]:


soup_2 = bs4.BeautifulSoup(requests.get(url_2).text, 'html5lib')
review_general_2 = soup_2.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_2 = review_general_2.find_all('div', attrs={'class': 'a-section review'})
review_title_2 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_2]
review_body_2 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_2]
review_stars_2 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_2]
review_date_2 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_2]
review_title_2, review_body_2, review_stars_2, review_date_2


# In[7]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_3 = url+str(3)
soup_3 = bs4.BeautifulSoup(requests.get(url_3).text, 'html5lib')
review_general_3 = soup_3.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_3 = review_general_3.find_all('div', attrs={'class': 'a-section review'})
review_title_3 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_3]
review_body_3 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_3]
review_stars_3 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_3]
review_date_3 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_3]
review_title_3, review_body_3, review_stars_3, review_date_3


# In[8]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_4 = url+str(4)
soup_4 = bs4.BeautifulSoup(requests.get(url_4).text, 'html5lib')
review_general_4 = soup_4.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_4 = review_general_4.find_all('div', attrs={'class': 'a-section review'})
review_title_4 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_4]
review_body_4 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_4]
review_stars_4 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_4]
review_date_4 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_4]
review_title_4, review_body_4, review_stars_4, review_date_4


# In[9]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_5 = url+str(5)
soup_5 = bs4.BeautifulSoup(requests.get(url_5).text, 'html5lib')
review_general_5 = soup_5.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_5 = review_general_5.find_all('div', attrs={'class': 'a-section review'})
review_title_5 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_5]
review_body_5 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_5]
review_stars_5 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_5]
review_date_5 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_5]
review_title_5, review_body_5, review_stars_5, review_date_5


# In[11]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_6 = url+str(6)
soup_6 = bs4.BeautifulSoup(requests.get(url_6).text, 'html5lib')
review_general_6 = soup_6.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_6 = review_general_6.find_all('div', attrs={'class': 'a-section review'})
review_title_6 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_6]
review_body_6 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_6]
review_stars_6 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_6]
review_date_6 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_6]
review_title_6, review_body_6, review_stars_6, review_date_6


# In[13]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_7 = url+str(7)
soup_7 = bs4.BeautifulSoup(requests.get(url_7).text, 'html5lib')
review_general_7 = soup_7.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_7 = review_general_7.find_all('div', attrs={'class': 'a-section review'})
review_title_7 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_7]
review_body_7 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_7]
review_stars_7 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_7]
review_date_7 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_7]
review_title_7, review_body_7, review_stars_7, review_date_7


# In[14]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_8 = url+str(8)
soup_8 = bs4.BeautifulSoup(requests.get(url_8).text, 'html5lib')
review_general_8 = soup_8.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_8 = review_general_8.find_all('div', attrs={'class': 'a-section review'})
review_title_8 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_8]
review_body_8 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_8]
review_stars_8 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_8]
review_date_8 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_8]
review_title_8, review_body_8, review_stars_8, review_date_8


# In[15]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_9 = url+str(9)
soup_9 = bs4.BeautifulSoup(requests.get(url_9).text, 'html5lib')
review_general_9 = soup_9.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_9 = review_general_9.find_all('div', attrs={'class': 'a-section review'})
review_title_9 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_9]
review_body_9 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_9]
review_stars_9 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_9]
review_date_9 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_9]
review_title_9, review_body_9, review_stars_9, review_date_9


# In[16]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_10 = url+str(10)
soup_10 = bs4.BeautifulSoup(requests.get(url_10).text, 'html5lib')
review_general_10 = soup_10.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_10 = review_general_10.find_all('div', attrs={'class': 'a-section review'})
review_title_10 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_10]
review_body_10 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_10]
review_stars_10 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_10]
review_date_10 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_10]
review_title_10, review_body_10, review_stars_10, review_date_10


# In[17]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_11 = url+str(11)
soup_11 = bs4.BeautifulSoup(requests.get(url_11).text, 'html5lib')
review_general_11 = soup_11.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_11 = review_general_11.find_all('div', attrs={'class': 'a-section review'})
review_title_11 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_11]
review_body_11 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_11]
review_stars_11 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_11]
review_date_11 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_11]
review_title_11, review_body_11, review_stars_11, review_date_11


# In[19]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_12 = url+str(12)
soup_12 = bs4.BeautifulSoup(requests.get(url_12).text, 'html5lib')
review_general_12 = soup_12.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_12 = review_general_12.find_all('div', attrs={'class': 'a-section review'})
review_title_12 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_12]
review_body_12 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_12]
review_stars_12 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_12]
review_date_12 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_12]
review_title_12, review_body_12, review_stars_12, review_date_12


# In[21]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_13 = url+str(13)
soup_13 = bs4.BeautifulSoup(requests.get(url_13).text, 'html5lib')
review_general_13 = soup_13.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_13 = review_general_13.find_all('div', attrs={'class': 'a-section review'})
review_title_13 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_13]
review_body_13 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_13]
review_stars_13 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_13]
review_date_13 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_13]
review_title_13, review_body_13, review_stars_13, review_date_13


# In[23]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_14 = url+str(14)
soup_14 = bs4.BeautifulSoup(requests.get(url_14).text, 'html5lib')
review_general_14 = soup_14.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_14 = review_general_14.find_all('div', attrs={'class': 'a-section review'})
review_title_14 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_14]
review_body_14 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_14]
review_stars_14 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_14]
review_date_14 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_14]
review_title_14, review_body_14, review_stars_14, review_date_14


# In[24]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_15 = url+str(15)
soup_15 = bs4.BeautifulSoup(requests.get(url_15).text, 'html5lib')
review_general_15 = soup_15.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_15 = review_general_15.find_all('div', attrs={'class': 'a-section review'})
review_title_15 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_15]
review_body_15 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_15]
review_stars_15 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_15]
review_date_15 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_15]
review_title_15, review_body_15, review_stars_15, review_date_15


# In[25]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_16 = url+str(16)
soup_16 = bs4.BeautifulSoup(requests.get(url_16).text, 'html5lib')
review_general_16 = soup_16.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_16 = review_general_16.find_all('div', attrs={'class': 'a-section review'})
review_title_16 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_16]
review_body_16 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_16]
review_stars_16 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_16]
review_date_16 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_16]
review_title_16, review_body_16, review_stars_16, review_date_16


# In[26]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_17 = url+str(17)
soup_17 = bs4.BeautifulSoup(requests.get(url_17).text, 'html5lib')
review_general_17 = soup_17.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_17 = review_general_17.find_all('div', attrs={'class': 'a-section review'})
review_title_17 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_17]
review_body_17 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_17]
review_stars_17 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_17]
review_date_17 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_17]
review_title_17, review_body_17, review_stars_17, review_date_17


# In[29]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_18 = url+str(18)
soup_18 = bs4.BeautifulSoup(requests.get(url_18).text, 'html5lib')
review_general_18 = soup_18.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_18 = review_general_18.find_all('div', attrs={'class': 'a-section review'})
review_title_18 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_18]
review_body_18 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_18]
review_stars_18 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_18]
review_date_18 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_18]
review_title_18, review_body_18, review_stars_18, review_date_18


# In[33]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_19 = url+str(19)
soup_19 = bs4.BeautifulSoup(requests.get(url_19).text, 'html5lib')
review_general_19 = soup_19.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_19 = review_general_19.find_all('div', attrs={'class': 'a-section review'})
review_title_19 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_19]
review_body_19 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_19]
review_stars_19 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_19]
review_date_19 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_19]
review_title_19, review_body_19, review_stars_19, review_date_19


# In[34]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_20 = url+str(20)
soup_20 = bs4.BeautifulSoup(requests.get(url_20).text, 'html5lib')
review_general_20 = soup_20.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_20 = review_general_20.find_all('div', attrs={'class': 'a-section review'})
review_title_20 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_20]
review_body_20 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_20]
review_stars_20 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_20]
review_date_20 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_20]
review_title_20, review_body_20, review_stars_20, review_date_20


# In[35]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_21 = url+str(21)
soup_21 = bs4.BeautifulSoup(requests.get(url_21).text, 'html5lib')
review_general_21 = soup_21.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_21 = review_general_21.find_all('div', attrs={'class': 'a-section review'})
review_title_21 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_21]
review_body_21 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_21]
review_stars_21 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_21]
review_date_21 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_21]
review_title_21, review_body_21, review_stars_21, review_date_21


# In[37]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_22 = url+str(22)
soup_22 = bs4.BeautifulSoup(requests.get(url_22).text, 'html5lib')
review_general_22 = soup_22.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_22 = review_general_22.find_all('div', attrs={'class': 'a-section review'})
review_title_22 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text.strip() for s in review_section_22]
review_body_22 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_22]
review_stars_22 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_22]
review_date_22 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_22]
review_title_22, review_body_22, review_stars_22, review_date_22


# In[38]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_23 = url+str(23)
soup_23 = bs4.BeautifulSoup(requests.get(url_23).text, 'html5lib')
review_general_23 = soup_23.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_23 = review_general_23.find_all('div', attrs={'class': 'a-section review'})
review_title_23 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}).
                 text.strip() for s in review_section_23]
review_body_23 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_23]
review_stars_23 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_23]
review_date_23 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_23]
review_title_23, review_body_23, review_stars_23, review_date_23


# In[39]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_24 = url+str(24)
soup_24 = bs4.BeautifulSoup(requests.get(url_24).text, 'html5lib')
review_general_24 = soup_24.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_24 = review_general_24.find_all('div', attrs={'class': 'a-section review'})
review_title_24 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_24]
review_body_24 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_24]
review_stars_24 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_24]
review_date_24 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_24]
review_title_24, review_body_24, review_stars_24, review_date_24


# In[40]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_25 = url+str(25)
soup_25 = bs4.BeautifulSoup(requests.get(url_25).text, 'html5lib')
review_general_25 = soup_25.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_25 = review_general_25.find_all('div', attrs={'class': 'a-section review'})
review_title_25 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_25]
review_body_25 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_25]
review_stars_25 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_25]
review_date_25 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_25]
review_title_25, review_body_25, review_stars_25, review_date_25


# In[42]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_26 = url+str(26)
soup_26 = bs4.BeautifulSoup(requests.get(url_26).text, 'html5lib')
review_general_26 = soup_26.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_26 = review_general_26.find_all('div', attrs={'class': 'a-section review'})
review_title_26 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_26]
review_body_26 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_26]
review_stars_26 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_26]
review_date_26 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_26]
review_title_26, review_body_26, review_stars_26, review_date_26


# In[43]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_27 = url+str(27)
soup_27 = bs4.BeautifulSoup(requests.get(url_27).text, 'html5lib')
review_general_27 = soup_27.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_27 = review_general_27.find_all('div', attrs={'class': 'a-section review'})
review_title_27 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_27]
review_body_27 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_27]
review_stars_27 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_27]
review_date_27 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_27]
review_title_27, review_body_27, review_stars_27, review_date_27


# In[45]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_28 = url+str(28)
soup_28 = bs4.BeautifulSoup(requests.get(url_28).text, 'html5lib')
review_general_28 = soup_28.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_28 = review_general_28.find_all('div', attrs={'class': 'a-section review'})
review_title_28 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_28]
review_body_28 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_28]
review_stars_28 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_28]
review_date_28 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_28]
review_title_28, review_body_28, review_stars_28, review_date_28


# In[46]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_29 = url+str(29)
soup_29 = bs4.BeautifulSoup(requests.get(url_29).text, 'html5lib')
review_general_29 = soup_29.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_29 = review_general_29.find_all('div', attrs={'class': 'a-section review'})
review_title_29 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_29]
review_body_29 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_29]
review_stars_29 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_29]
review_date_29 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_29]
review_title_29, review_body_29, review_stars_29, review_date_29


# In[47]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_30 = url+str(30)
soup_30 = bs4.BeautifulSoup(requests.get(url_30).text, 'html5lib')
review_general_30 = soup_30.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_30 = review_general_30.find_all('div', attrs={'class': 'a-section review'})
review_title_30 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_30]
review_body_30 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_30]
review_stars_30 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_30]
review_date_30 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_30]
review_title_30, review_body_30, review_stars_30, review_date_30


# In[50]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_31 = url+str(31)
soup_31 = bs4.BeautifulSoup(requests.get(url_31).text, 'html5lib')
review_general_31 = soup_31.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_31 = review_general_31.find_all('div', attrs={'class': 'a-section review'})
review_title_31 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_31]
review_body_31 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_31]
review_stars_31 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_31]
review_date_31 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_31]
review_title_31, review_body_31, review_stars_31, review_date_31


# In[53]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_32 = url+str(32)
soup_32 = bs4.BeautifulSoup(requests.get(url_32).text, 'html5lib')
review_general_32 = soup_32.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_32 = review_general_32.find_all('div', attrs={'class': 'a-section review'})
review_title_32 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_32]
review_body_32 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_32]
review_stars_32 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_32]
review_date_32 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_32]
review_title_32, review_body_32, review_stars_32, review_date_32


# In[54]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_33 = url+str(33)
soup_33 = bs4.BeautifulSoup(requests.get(url_33).text, 'html5lib')
review_general_33 = soup_33.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_33 = review_general_33.find_all('div', attrs={'class': 'a-section review'})
review_title_33 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_33]
review_body_33 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_33]
review_stars_33 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_33]
review_date_33 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_33]
review_title_33, review_body_33, review_stars_33, review_date_33


# In[55]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_34 = url+str(34)
soup_34 = bs4.BeautifulSoup(requests.get(url_34).text, 'html5lib')
review_general_34 = soup_34.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_34 = review_general_34.find_all('div', attrs={'class': 'a-section review'})
review_title_34 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_34]
review_body_34 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_34]
review_stars_34 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_34]
review_date_34 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_34]
review_title_34, review_body_34, review_stars_34, review_date_34


# In[56]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_35 = url+str(35)
soup_35 = bs4.BeautifulSoup(requests.get(url_35).text, 'html5lib')
review_general_35 = soup_35.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_35 = review_general_35.find_all('div', attrs={'class': 'a-section review'})
review_title_35 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_35]
review_body_35 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_35]
review_stars_35 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_35]
review_date_35 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_35]
review_title_35, review_body_35, review_stars_35, review_date_35


# In[59]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_36 = url+str(36)
soup_36 = bs4.BeautifulSoup(requests.get(url_36).text, 'html5lib')
review_general_36 = soup_36.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_36 = review_general_36.find_all('div', attrs={'class': 'a-section review'})
review_title_36 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_36]
review_body_36 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_36]
review_stars_36 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_36]
review_date_36 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_36]
review_title_36, review_body_36, review_stars_36, review_date_36


# In[60]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_37 = url+str(37)
soup_37 = bs4.BeautifulSoup(requests.get(url_37).text, 'html5lib')
review_general_37 = soup_37.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_37 = review_general_37.find_all('div', attrs={'class': 'a-section review'})
review_title_37 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_37]
review_body_37 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_37]
review_stars_37 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_37]
review_date_37 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_37]
review_title_37, review_body_37, review_stars_37, review_date_37


# In[61]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_38 = url+str(38)
soup_38 = bs4.BeautifulSoup(requests.get(url_38).text, 'html5lib')
review_general_38 = soup_38.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_38 = review_general_38.find_all('div', attrs={'class': 'a-section review'})
review_title_38 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_38]
review_body_38 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_38]
review_stars_38 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_38]
review_date_38 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_38]
review_title_38, review_body_38, review_stars_38, review_date_38


# In[62]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_39 = url+str(39)
soup_39 = bs4.BeautifulSoup(requests.get(url_39).text, 'html5lib')
review_general_39 = soup_39.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_39 = review_general_39.find_all('div', attrs={'class': 'a-section review'})
review_title_39 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_39]
review_body_39 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_39]
review_stars_39 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_39]
review_date_39 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_39]
review_title_39, review_body_39, review_stars_39, review_date_39


# In[63]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_40 = url+str(40)
soup_40 = bs4.BeautifulSoup(requests.get(url_40).text, 'html5lib')
review_general_40 = soup_40.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_40 = review_general_40.find_all('div', attrs={'class': 'a-section review'})
review_title_40 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_40]
review_body_40 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_40]
review_stars_40 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_40]
review_date_40 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_40]
review_title_40, review_body_40, review_stars_40, review_date_40


# In[64]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_41 = url+str(41)
soup_41 = bs4.BeautifulSoup(requests.get(url_41).text, 'html5lib')
review_general_41 = soup_41.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_41 = review_general_41.find_all('div', attrs={'class': 'a-section review'})
review_title_41 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_41]
review_body_41 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_41]
review_stars_41 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_41]
review_date_41 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_41]
review_title_41, review_body_41, review_stars_41, review_date_41


# In[65]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_42 = url+str(42)
soup_42 = bs4.BeautifulSoup(requests.get(url_42).text, 'html5lib')
review_general_42 = soup_42.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_42 = review_general_42.find_all('div', attrs={'class': 'a-section review'})
review_title_42 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_42]
review_body_42 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_42]
review_stars_42 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_42]
review_date_42 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_42]
review_title_42, review_body_42, review_stars_42, review_date_42


# In[66]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_43 = url+str(43)
soup_43 = bs4.BeautifulSoup(requests.get(url_43).text, 'html5lib')
review_general_43 = soup_43.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_43 = review_general_43.find_all('div', attrs={'class': 'a-section review'})
review_title_43 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_43]
review_body_43 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_43]
review_stars_43 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_43]
review_date_43 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_43]
review_title_43, review_body_43, review_stars_43, review_date_43


# In[67]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_44 = url+str(44)
soup_44 = bs4.BeautifulSoup(requests.get(url_44).text, 'html5lib')
review_general_44 = soup_44.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_44 = review_general_44.find_all('div', attrs={'class': 'a-section review'})
review_title_44 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_44]
review_body_44 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_44]
review_stars_44 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_44]
review_date_44 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_44]
review_title_44, review_body_44, review_stars_44, review_date_44


# In[69]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_45 = url+str(45)
soup_45 = bs4.BeautifulSoup(requests.get(url_45).text, 'html5lib')
review_general_45 = soup_45.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_45 = review_general_45.find_all('div', attrs={'class': 'a-section review'})
review_title_45 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_45]
review_body_45 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_45]
review_stars_45 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_45]
review_date_45 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_45]
review_title_45, review_body_45, review_stars_45, review_date_45


# In[70]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_46 = url+str(46)
soup_46 = bs4.BeautifulSoup(requests.get(url_46).text, 'html5lib')
review_general_46 = soup_46.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_46 = review_general_46.find_all('div', attrs={'class': 'a-section review'})
review_title_46 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_46]
review_body_46 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_46]
review_stars_46 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_46]
review_date_46 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_46]
review_title_46, review_body_46, review_stars_46, review_date_46


# In[71]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_47 = url+str(47)
soup_47 = bs4.BeautifulSoup(requests.get(url_47).text, 'html5lib')
review_general_47 = soup_47.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_47 = review_general_47.find_all('div', attrs={'class': 'a-section review'})
review_title_47= [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_47]
review_body_47 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_47]
review_stars_47 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_47]
review_date_47 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_47]
review_title_47, review_body_47, review_stars_47, review_date_47


# In[74]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_48 = url+str(48)
soup_48 = bs4.BeautifulSoup(requests.get(url_48).text, 'html5lib')
review_general_48 = soup_48.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_48 = review_general_48.find_all('div', attrs={'class': 'a-section review'})
review_title_48 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_48]
review_body_48 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_48]
review_stars_48 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_48]
review_date_48 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_48]
review_title_48, review_body_48, review_stars_48, review_date_48


# In[75]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_49 = url+str(49)
soup_49 = bs4.BeautifulSoup(requests.get(url_49).text, 'html5lib')
review_general_49 = soup_49.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_49 = review_general_49.find_all('div', attrs={'class': 'a-section review'})
review_title_49 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_49]
review_body_49 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_49]
review_stars_49 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_49]
review_date_49 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_49]
review_title_49, review_body_49, review_stars_49, review_date_49


# In[76]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_50 = url+str(50)
soup_50 = bs4.BeautifulSoup(requests.get(url_50).text, 'html5lib')
review_general_50 = soup_50.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_50 = review_general_50.find_all('div', attrs={'class': 'a-section review'})
review_title_50 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_50]
review_body_50 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_50]
review_stars_50 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_50]
review_date_50 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_50]
review_title_50, review_body_50, review_stars_50, review_date_50


# In[77]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_51 = url+str(51)
soup_51 = bs4.BeautifulSoup(requests.get(url_51).text, 'html5lib')
review_general_51 = soup_51.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_51 = review_general_51.find_all('div', attrs={'class': 'a-section review'})
review_title_51 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_51]
review_body_51 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_51]
review_stars_51 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_51]
review_date_51= [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_51]
review_title_51, review_body_51, review_stars_51, review_date_51


# In[79]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_52 = url+str(52)
soup_52 = bs4.BeautifulSoup(requests.get(url_52).text, 'html5lib')
review_general_52 = soup_52.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_52 = review_general_52.find_all('div', attrs={'class': 'a-section review'})
review_title_52 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_52]
review_body_52 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_52]
review_stars_52 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_52]
review_date_52 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_52]
review_title_52, review_body_52, review_stars_52, review_date_52


# In[80]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_53 = url+str(53)
soup_53 = bs4.BeautifulSoup(requests.get(url_53).text, 'html5lib')
review_general_53 = soup_53.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_53 = review_general_53.find_all('div', attrs={'class': 'a-section review'})
review_title_53 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_53]
review_body_53 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_53]
review_stars_53 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_53]
review_date_53 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_53]
review_title_53, review_body_53, review_stars_53, review_date_53


# In[81]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_54 = url+str(54)
soup_54 = bs4.BeautifulSoup(requests.get(url_54).text, 'html5lib')
review_general_54 = soup_54.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_54 = review_general_54.find_all('div', attrs={'class': 'a-section review'})
review_title_54 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_54]
review_body_54 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_54]
review_stars_54 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_54]
review_date_54 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_54]
review_title_54, review_body_54, review_stars_54, review_date_54


# In[82]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_55 = url+str(55)
soup_55 = bs4.BeautifulSoup(requests.get(url_55).text, 'html5lib')
review_general_55 = soup_55.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_55 = review_general_55.find_all('div', attrs={'class': 'a-section review'})
review_title_55 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_55]
review_body_55 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_55]
review_stars_55 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_55]
review_date_55= [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_55]
review_title_55, review_body_55, review_stars_55, review_date_55


# In[83]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_56 = url+str(56)
soup_56 = bs4.BeautifulSoup(requests.get(url_56).text, 'html5lib')
review_general_56 = soup_56.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_56 = review_general_56.find_all('div', attrs={'class': 'a-section review'})
review_title_56 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_56]
review_body_56 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_56]
review_stars_56 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_56]
review_date_56 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_56]
review_title_56, review_body_56, review_stars_56, review_date_56


# In[85]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_57 = url+str(57)
soup_57 = bs4.BeautifulSoup(requests.get(url_57).text, 'html5lib')
review_general_57 = soup_57.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_57 = review_general_57.find_all('div', attrs={'class': 'a-section review'})
review_title_57 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_57]
review_body_57 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_57]
review_stars_57 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_57]
review_date_57 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_57]
review_title_57, review_body_57, review_stars_57, review_date_57


# In[86]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_58 = url+str(58)
soup_58 = bs4.BeautifulSoup(requests.get(url_58).text, 'html5lib')
review_general_58 = soup_58.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_58 = review_general_58.find_all('div', attrs={'class': 'a-section review'})
review_title_58 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_58]
review_body_58 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_58]
review_stars_58 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_58]
review_date_58 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_58]
review_title_58, review_body_58, review_stars_58, review_date_58


# In[87]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_59 = url+str(59)
soup_59 = bs4.BeautifulSoup(requests.get(url_59).text, 'html5lib')
review_general_59 = soup_59.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_59 = review_general_59.find_all('div', attrs={'class': 'a-section review'})
review_title_59 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_59]
review_body_59 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_59]
review_stars_59 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_59]
review_date_59 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_59]
review_title_59, review_body_59, review_stars_59, review_date_59


# In[88]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_60 = url+str(60)
soup_60 = bs4.BeautifulSoup(requests.get(url_60).text, 'html5lib')
review_general_60 = soup_60.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_60 = review_general_60.find_all('div', attrs={'class': 'a-section review'})
review_title_60 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_60]
review_body_60 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_60]
review_stars_60 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_60]
review_date_60 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_60]
review_title_60, review_body_60, review_stars_60, review_date_60


# In[90]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_61 = url+str(61)
soup_61 = bs4.BeautifulSoup(requests.get(url_61).text, 'html5lib')
review_general_61 = soup_61.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_61 = review_general_61.find_all('div', attrs={'class': 'a-section review'})
review_title_61 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_61]
review_body_61 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_61]
review_stars_61 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_61]
review_date_61 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_61]
review_title_61, review_body_61, review_stars_61, review_date_61


# In[91]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_62 = url+str(62)
soup_62 = bs4.BeautifulSoup(requests.get(url_62).text, 'html5lib')
review_general_62 = soup_62.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_62 = review_general_62.find_all('div', attrs={'class': 'a-section review'})
review_title_62 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_62]
review_body_62 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_62]
review_stars_62 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_62]
review_date_62 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_62]
review_title_62, review_body_62, review_stars_62, review_date_62


# In[92]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_63 = url+str(63)
soup_63 = bs4.BeautifulSoup(requests.get(url_63).text, 'html5lib')
review_general_63 = soup_63.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_63 = review_general_63.find_all('div', attrs={'class': 'a-section review'})
review_title_63 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_63]
review_body_63 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_63]
review_stars_63 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_63]
review_date_63 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_63]
review_title_63, review_body_63, review_stars_63, review_date_63


# In[93]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_64 = url+str(64)
soup_64 = bs4.BeautifulSoup(requests.get(url_64).text, 'html5lib')
review_general_64 = soup_64.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_64 = review_general_64.find_all('div', attrs={'class': 'a-section review'})
review_title_64 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_64]
review_body_64 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_64]
review_stars_64 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_64]
review_date_64 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_64]
review_title_64, review_body_64, review_stars_64, review_date_64


# In[94]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_65 = url+str(65)
soup_65 = bs4.BeautifulSoup(requests.get(url_65).text, 'html5lib')
review_general_65 = soup_65.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_65 = review_general_65.find_all('div', attrs={'class': 'a-section review'})
review_title_65 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_65]
review_body_65 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_65]
review_stars_65 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_65]
review_date_65 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_65]
review_title_65, review_body_65, review_stars_65, review_date_65


# In[95]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_66 = url+str(66)
soup_66 = bs4.BeautifulSoup(requests.get(url_66).text, 'html5lib')
review_general_66 = soup_66.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_66 = review_general_66.find_all('div', attrs={'class': 'a-section review'})
review_title_66 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_66]
review_body_66 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_66]
review_stars_66 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_66]
review_date_66 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_66]
review_title_66, review_body_66, review_stars_66, review_date_66


# In[96]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_67 = url+str(67)
soup_67 = bs4.BeautifulSoup(requests.get(url_67).text, 'html5lib')
review_general_67 = soup_67.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_67 = review_general_67.find_all('div', attrs={'class': 'a-section review'})
review_title_67 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_67]
review_body_67 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_67]
review_stars_67 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_67]
review_date_67 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_67]
review_title_67, review_body_67, review_stars_67, review_date_67


# In[97]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_68 = url+str(68)
soup_68 = bs4.BeautifulSoup(requests.get(url_68).text, 'html5lib')
review_general_68 = soup_68.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_68 = review_general_68.find_all('div', attrs={'class': 'a-section review'})
review_title_68 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_68]
review_body_68 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_68]
review_stars_68 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_68]
review_date_68 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_68]
review_title_68, review_body_68, review_stars_68, review_date_68


# In[98]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_69 = url+str(69)
soup_69 = bs4.BeautifulSoup(requests.get(url_69).text, 'html5lib')
review_general_69 = soup_69.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_69 = review_general_69.find_all('div', attrs={'class': 'a-section review'})
review_title_69 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_69]
review_body_69 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_69]
review_stars_69 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_69]
review_date_69 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_69]
review_title_69, review_body_69, review_stars_69, review_date_69


# In[99]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_70 = url+str(70)
soup_70 = bs4.BeautifulSoup(requests.get(url_70).text, 'html5lib')
review_general_70 = soup_70.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_70 = review_general_70.find_all('div', attrs={'class': 'a-section review'})
review_title_70 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_70]
review_body_70 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_70]
review_stars_70 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_70]
review_date_70 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_70]
review_title_70, review_body_70, review_stars_70, review_date_70


# In[100]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_71 = url+str(71)
soup_71 = bs4.BeautifulSoup(requests.get(url_71).text, 'html5lib')
review_general_71 = soup_71.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_71 = review_general_71.find_all('div', attrs={'class': 'a-section review'})
review_title_71 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_71]
review_body_71 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_71]
review_stars_71 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_71]
review_date_71 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_71]
review_title_71, review_body_71, review_stars_71, review_date_71


# In[101]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_72 = url+str(72)
soup_72 = bs4.BeautifulSoup(requests.get(url_72).text, 'html5lib')
review_general_72 = soup_72.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_72 = review_general_72.find_all('div', attrs={'class': 'a-section review'})
review_title_72 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_72]
review_body_72 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_72]
review_stars_72 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_72]
review_date_72 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_72]
review_title_72, review_body_72, review_stars_72, review_date_72


# In[103]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_73 = url+str(73)
soup_73 = bs4.BeautifulSoup(requests.get(url_73).text, 'html5lib')
review_general_73 = soup_73.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_73 = review_general_73.find_all('div', attrs={'class': 'a-section review'})
review_title_73 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_73]
review_body_73 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_73]
review_stars_73 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_73]
review_date_73 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_73]
review_title_73, review_body_73, review_stars_73, review_date_73


# In[104]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_74 = url+str(74)
soup_74 = bs4.BeautifulSoup(requests.get(url_74).text, 'html5lib')
review_general_74 = soup_74.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_74 = review_general_74.find_all('div', attrs={'class': 'a-section review'})
review_title_74 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_74]
review_body_74 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_74]
review_stars_74 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_74]
review_date_74 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_74]
review_title_74, review_body_74, review_stars_74, review_date_74


# In[105]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_75 = url+str(75)
soup_75 = bs4.BeautifulSoup(requests.get(url_75).text, 'html5lib')
review_general_75 = soup_75.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_75 = review_general_75.find_all('div', attrs={'class': 'a-section review'})
review_title_75 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_75]
review_body_75 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_75]
review_stars_75 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_75]
review_date_75 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_75]
review_title_75, review_body_75, review_stars_75, review_date_75


# In[106]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_76 = url+str(76)
soup_76 = bs4.BeautifulSoup(requests.get(url_76).text, 'html5lib')
review_general_76 = soup_76.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_76 = review_general_76.find_all('div', attrs={'class': 'a-section review'})
review_title_76 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_76]
review_body_76 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_76]
review_stars_76 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_76]
review_date_76 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_76]
review_title_76, review_body_76, review_stars_76, review_date_76


# In[107]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_77 = url+str(77)
soup_77 = bs4.BeautifulSoup(requests.get(url_77).text, 'html5lib')
review_general_77 = soup_77.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_77 = review_general_77.find_all('div', attrs={'class': 'a-section review'})
review_title_77 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_77]
review_body_77 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_77]
review_stars_77 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_77]
review_date_77 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_77]
review_title_77, review_body_77, review_stars_77, review_date_77


# In[108]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_78 = url+str(78)
soup_78 = bs4.BeautifulSoup(requests.get(url_78).text, 'html5lib')
review_general_78 = soup_78.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_78 = review_general_78.find_all('div', attrs={'class': 'a-section review'})
review_title_78 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_78]
review_body_78 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_78]
review_stars_78 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_78]
review_date_78 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_78]
review_title_78, review_body_78, review_stars_78, review_date_78


# In[109]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_79 = url+str(79)
soup_79 = bs4.BeautifulSoup(requests.get(url_79).text, 'html5lib')
review_general_79 = soup_79.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_79 = review_general_79.find_all('div', attrs={'class': 'a-section review'})
review_title_79 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_79]
review_body_79 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_79]
review_stars_79 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_79]
review_date_79 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_79]
review_title_79, review_body_79, review_stars_79, review_date_79


# In[110]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_80 = url+str(80)
soup_80 = bs4.BeautifulSoup(requests.get(url_80).text, 'html5lib')
review_general_80 = soup_80.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_80 = review_general_80.find_all('div', attrs={'class': 'a-section review'})
review_title_80 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_80]
review_body_80 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_80]
review_stars_80 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_80]
review_date_80 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_80]
review_title_80, review_body_80, review_stars_80, review_date_80


# In[111]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_81 = url+str(81)
soup_81 = bs4.BeautifulSoup(requests.get(url_81).text, 'html5lib')
review_general_81 = soup_81.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_81 = review_general_81.find_all('div', attrs={'class': 'a-section review'})
review_title_81 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_81]
review_body_81 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_81]
review_stars_81 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_81]
review_date_81 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_81]
review_title_81, review_body_81, review_stars_81, review_date_81


# In[112]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_82 = url+str(82)
soup_82 = bs4.BeautifulSoup(requests.get(url_82).text, 'html5lib')
review_general_82 = soup_82.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_82 = review_general_82.find_all('div', attrs={'class': 'a-section review'})
review_title_82 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_82]
review_body_82 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_82]
review_stars_82 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_82]
review_date_82 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_82]
review_title_82, review_body_82, review_stars_82, review_date_82


# In[114]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_83 = url+str(83)
soup_83 = bs4.BeautifulSoup(requests.get(url_83).text, 'html5lib')
review_general_83 = soup_83.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_83 = review_general_83.find_all('div', attrs={'class': 'a-section review'})
review_title_83 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_83]
review_body_83 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_83]
review_stars_83 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_83]
review_date_83 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_83]
review_title_83, review_body_83, review_stars_83, review_date_83


# In[115]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_84 = url+str(84)
soup_84 = bs4.BeautifulSoup(requests.get(url_84).text, 'html5lib')
review_general_84 = soup_84.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_84 = review_general_84.find_all('div', attrs={'class': 'a-section review'})
review_title_84 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_84]
review_body_84 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_84]
review_stars_84 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_84]
review_date_84 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_84]
review_title_84, review_body_84, review_stars_84, review_date_84


# In[116]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_85 = url+str(85)
soup_85 = bs4.BeautifulSoup(requests.get(url_85).text, 'html5lib')
review_general_85 = soup_85.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_85 = review_general_85.find_all('div', attrs={'class': 'a-section review'})
review_title_85 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_85]
review_body_85 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_85]
review_stars_85 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_85]
review_date_85 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_85]
review_title_85, review_body_85, review_stars_85, review_date_85


# In[117]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_86 = url+str(86)
soup_86 = bs4.BeautifulSoup(requests.get(url_86).text, 'html5lib')
review_general_86 = soup_86.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_86 = review_general_86.find_all('div', attrs={'class': 'a-section review'})
review_title_86 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_86]
review_body_86 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_86]
review_stars_86 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_86]
review_date_86 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_86]
review_title_86, review_body_86, review_stars_86, review_date_86


# In[118]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_87 = url+str(87)
soup_87 = bs4.BeautifulSoup(requests.get(url_87).text, 'html5lib')
review_general_87 = soup_87.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_87 = review_general_87.find_all('div', attrs={'class': 'a-section review'})
review_title_87 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_87]
review_body_87 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_87]
review_stars_87 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_87]
review_date_87 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_87]
review_title_87, review_body_87, review_stars_87, review_date_87


# In[119]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_88 = url+str(88)
soup_88 = bs4.BeautifulSoup(requests.get(url_88).text, 'html5lib')
review_general_88 = soup_88.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_88 = review_general_88.find_all('div', attrs={'class': 'a-section review'})
review_title_88 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_88]
review_body_88 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_88]
review_stars_88 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_88]
review_date_88 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_88]
review_title_88, review_body_88, review_stars_88, review_date_88


# In[120]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_89 = url+str(89)
soup_89 = bs4.BeautifulSoup(requests.get(url_89).text, 'html5lib')
review_general_89 = soup_89.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_89 = review_general_89.find_all('div', attrs={'class': 'a-section review'})
review_title_89 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_89]
review_body_89 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_89]
review_stars_89 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_89]
review_date_89 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_89]
review_title_89, review_body_89, review_stars_89, review_date_89


# In[122]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_90 = url+str(90)
soup_90 = bs4.BeautifulSoup(requests.get(url_90).text, 'html5lib')
review_general_90 = soup_90.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_90 = review_general_90.find_all('div', attrs={'class': 'a-section review'})
review_title_90 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_90]
review_body_90 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_90]
review_stars_90 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_90]
review_date_90 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_90]
review_title_90, review_body_90, review_stars_90, review_date_90


# In[123]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_91 = url+str(91)
soup_91 = bs4.BeautifulSoup(requests.get(url_91).text, 'html5lib')
review_general_91 = soup_91.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_91 = review_general_91.find_all('div', attrs={'class': 'a-section review'})
review_title_91 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_91]
review_body_91 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_91]
review_stars_91 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_91]
review_date_91 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_91]
review_title_91, review_body_91, review_stars_91, review_date_91


# In[124]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_92 = url+str(92)
soup_92 = bs4.BeautifulSoup(requests.get(url_92).text, 'html5lib')
review_general_92 = soup_92.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_92 = review_general_92.find_all('div', attrs={'class': 'a-section review'})
review_title_92 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_92]
review_body_92 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_92]
review_stars_92 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_92]
review_date_92 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_92]
review_title_92, review_body_92, review_stars_92, review_date_92


# In[125]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_93 = url+str(93)
soup_93 = bs4.BeautifulSoup(requests.get(url_93).text, 'html5lib')
review_general_93 = soup_93.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_93 = review_general_93.find_all('div', attrs={'class': 'a-section review'})
review_title_93 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_93]
review_body_93 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_93]
review_stars_93 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_93]
review_date_93 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_93]
review_title_93, review_body_93, review_stars_93, review_date_93


# In[126]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_94 = url+str(94)
soup_94 = bs4.BeautifulSoup(requests.get(url_94).text, 'html5lib')
review_general_94 = soup_94.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_94 = review_general_94.find_all('div', attrs={'class': 'a-section review'})
review_title_94 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_94]
review_body_94 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_94]
review_stars_94 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_94]
review_date_94 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_94]
review_title_94, review_body_94, review_stars_94, review_date_94


# In[127]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_95 = url+str(95)
soup_95 = bs4.BeautifulSoup(requests.get(url_95).text, 'html5lib')
review_general_95 = soup_95.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_95 = review_general_95.find_all('div', attrs={'class': 'a-section review'})
review_title_95 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_95]
review_body_95 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_95]
review_stars_95 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_95]
review_date_95 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_95]
review_title_95, review_body_95, review_stars_95, review_date_95


# In[130]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_96 = url+str(96)
soup_96 = bs4.BeautifulSoup(requests.get(url_96).text, 'html5lib')
review_general_96 = soup_96.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_96 = review_general_96.find_all('div', attrs={'class': 'a-section review'})
review_title_96 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_96]
review_body_96 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_96]
review_stars_96 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_96]
review_date_96 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_96]
review_title_96, review_body_96, review_stars_96, review_date_96


# In[132]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_97 = url+str(97)
soup_97 = bs4.BeautifulSoup(requests.get(url_97).text, 'html5lib')
review_general_97 = soup_97.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_97 = review_general_97.find_all('div', attrs={'class': 'a-section review'})
review_title_97 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_97]
review_body_97 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_97]
review_stars_97 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_97]
review_date_97 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_97]
review_title_97, review_body_97, review_stars_97, review_date_97


# In[133]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_98 = url+str(98)
soup_98 = bs4.BeautifulSoup(requests.get(url_98).text, 'html5lib')
review_general_98 = soup_98.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_98 = review_general_98.find_all('div', attrs={'class': 'a-section review'})
review_title_98 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_98]
review_body_98 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_98]
review_stars_98 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_98]
review_date_98 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_98]
review_title_98, review_body_98, review_stars_98, review_date_98


# In[134]:


url = """https://www.amazon.com/RockBirds-Flashlights-Bright-Aluminum-Flashlight/product-reviews/B00X61AJYM/ref=cm_cr_getr_d_paging_btm_147?sortBy=recent&pageNumber="""
url_99 = url+str(99)
soup_99 = bs4.BeautifulSoup(requests.get(url_99).text, 'html5lib')
review_general_99 = soup_99.find('div', attrs={'class': 'a-section a-spacing-none review-views celwidget'})
review_section_99 = review_general_99.find_all('div', attrs={'class': 'a-section review'})
review_title_99 = [s.find('a', attrs={'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})
                 .text.strip() for s in review_section_99]
review_body_99 = [s.find('div', attrs={'class':'a-row review-data'}).text.strip() for s in review_section_99]
review_stars_99 = [s.find('span', attrs={'class':'a-icon-alt'}).text.strip() for s in review_section_99]
review_date_99 = [s.find('span', attrs={'class':'a-size-base a-color-secondary review-date'}).text.strip() for s in review_section_99]
review_title_99, review_body_99, review_stars_99, review_date_99


# In[135]:


import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np


# In[136]:


review_title = review_title_1 + review_title_2 + review_title_3 + review_title_4 + review_title_5 + review_title_6 + review_title_7 + review_title_8 + review_title_9 + review_title_10+ review_title_11 + review_title_12 + review_title_13 + review_title_14 + review_title_15 + review_title_16 + review_title_17 + review_title_18 + review_title_19 + review_title_20 + review_title_21 + review_title_22 + review_title_23 + review_title_24 + review_title_25 + review_title_26 + review_title_27 + review_title_28 + review_title_29 + review_title_30 + review_title_31 + review_title_32 + review_title_33 + review_title_34 + review_title_35 + review_title_36 + review_title_37 + review_title_38 + review_title_39 + review_title_40 + review_title_41 + review_title_42 + review_title_43 + review_title_44 + review_title_45 + review_title_46 + review_title_47 + review_title_48 + review_title_49 + review_title_50 + review_title_51 + review_title_52 + review_title_53 + review_title_54 + review_title_55 + review_title_56 + review_title_57 + review_title_58 + review_title_59 + review_title_60 + review_title_61 + review_title_62 + review_title_63 + review_title_64 + review_title_65 + review_title_66 + review_title_67 + review_title_68 + review_title_69 + review_title_70 + review_title_71 + review_title_72 + review_title_73 + review_title_74 + review_title_75 + review_title_76 + review_title_77 + review_title_78 + review_title_79 + review_title_80 + review_title_81 + review_title_82 + review_title_83 + review_title_84 + review_title_85 + review_title_86 + review_title_87 + review_title_88 + review_title_89 + review_title_90 + review_title_91 + review_title_92 + review_title_93 + review_title_94 + review_title_95 + review_title_96 + review_title_97 + review_title_98 + review_title_99


# In[137]:


review_stars = review_stars_1 + review_stars_2 + review_stars_3 + review_stars_4 + review_stars_5 + review_stars_6 + review_stars_7 + review_stars_8 + review_stars_9 + review_stars_10 + review_stars_11 + review_stars_12 + review_stars_13 + review_stars_14 + review_stars_15 + review_stars_16 + review_stars_17 + review_stars_18 + review_stars_19 + review_stars_20 + review_stars_21 + review_stars_22 + review_stars_23 + review_stars_24 + review_stars_25 + review_stars_26 + review_stars_27 + review_stars_28 + review_stars_29 + review_stars_30 + review_stars_31 + review_stars_32 + review_stars_33 + review_stars_34 + review_stars_35 + review_stars_36 + review_stars_37 + review_stars_38 + review_stars_39 + review_stars_40 + review_stars_41 + review_stars_42 + review_stars_43 + review_stars_44 + review_stars_45 + review_stars_46 + review_stars_47 + review_stars_48 + review_stars_49 + review_stars_50 + review_stars_51 + review_stars_52 + review_stars_53 + review_stars_54 + review_stars_55 + review_stars_56 + review_stars_57 + review_stars_58 + review_stars_59 + review_stars_60 + review_stars_61 + review_stars_62 + review_stars_63 + review_stars_64 + review_stars_65 + review_stars_66 + review_stars_67 + review_stars_68 + review_stars_69 + review_stars_70 + review_stars_71 + review_stars_72 + review_stars_73 + review_stars_74 + review_stars_75 + review_stars_76 + review_stars_77 + review_stars_78 + review_stars_79 + review_stars_80 + review_stars_81 + review_stars_82 + review_stars_83 + review_stars_84 + review_stars_85 + review_stars_86 + review_stars_87 + review_stars_88 + review_stars_89 + review_stars_90 + review_stars_91 + review_stars_92 + review_stars_93 + review_stars_94 + review_stars_95 + review_stars_96 + review_stars_97 + review_stars_98 + review_stars_99


# In[138]:


review_date = review_date_1 + review_date_2 + review_date_3 + review_date_4 + review_date_5 + review_date_6 + review_date_7 + review_date_8 + review_date_9 + review_date_10 + review_date_11 + review_date_12 + review_date_13 + review_date_14 + review_date_15 + review_date_16 + review_date_17 + review_date_18 + review_date_19 + review_date_20 + review_date_21 + review_date_22 + review_date_23 + review_date_24 + review_date_25 + review_date_26 + review_date_27 + review_date_28 + review_date_29 + review_date_30 + review_date_31 + review_date_32 + review_date_33 + review_date_34 + review_date_35 + review_date_36 + review_date_37 + review_date_38 + review_date_39 + review_date_40 + review_date_41 + review_date_42 + review_date_43 + review_date_44 + review_date_45 + review_date_46 + review_date_47 + review_date_48 + review_date_49 + review_date_50 + review_date_51 + review_date_52 + review_date_53 + review_date_54 + review_date_55 + review_date_56 + review_date_57 + review_date_58 + review_date_59 + review_date_60 + review_date_61 + review_date_62 + review_date_63 + review_date_64 + review_date_65 + review_date_66 + review_date_67 + review_date_68 + review_date_69 + review_date_70 + review_date_71 + review_date_72 + review_date_73 + review_date_74 + review_date_75 + review_date_76 + review_date_77 + review_date_78 + review_date_79 + review_date_80 + review_date_81 + review_date_82 + review_date_83 + review_date_84 + review_date_85 + review_date_86 + review_date_87 + review_date_88 + review_date_89 + review_date_90 + review_date_91 + review_date_92 + review_date_93 + review_date_94 + review_date_95 + review_date_96 + review_date_97 + review_date_98 + review_date_99


# In[139]:


review_body = review_body_1 + review_body_2 + review_body_3 + review_body_4 + review_body_5 + review_body_6 + review_body_7 + review_body_8 + review_body_9 + review_body_10 + review_body_11 + review_body_12 + review_body_13 + review_body_14 + review_body_15 + review_body_16 + review_body_17 + review_body_18 + review_body_19 + review_body_20 + review_body_21 + review_body_22 + review_body_23 + review_body_24 + review_body_25 + review_body_26 + review_body_27 + review_body_28 + review_body_29 + review_body_30 + review_body_31 + review_body_32 + review_body_33 + review_body_34 + review_body_35 + review_body_36 + review_body_37 + review_body_38 + review_body_39 + review_body_40 + review_body_41 + review_body_42 + review_body_43 + review_body_44 + review_body_45 + review_body_46 + review_body_47 + review_body_48 + review_body_49 + review_body_50 + review_body_51 + review_body_52 + review_body_53 + review_body_54 + review_body_55 + review_body_56 + review_body_57 + review_body_58 + review_body_59 + review_body_60 + review_body_61 + review_body_62 + review_body_63 + review_body_64 + review_body_65 + review_body_66 + review_body_67 + review_body_68 + review_body_69 + review_body_70 + review_body_71 + review_body_72 + review_body_73 + review_body_74 + review_body_75 + review_body_76 + review_body_77 + review_body_78 + review_body_79 + review_body_80 + review_body_81 + review_body_82 + review_body_83 + review_body_84 + review_body_85 + review_body_86 + review_body_87 + review_body_88 + review_body_89 + review_body_90 + review_body_91 + review_body_92 + review_body_93 + review_body_94 + review_body_95 + review_body_96 + review_body_97 + review_body_98 + review_body_99 


# In[140]:


df = pd.DataFrame(list(zip(review_title,review_stars, review_date,review_body)))
df.columns = ['review_title','review_stars','review_date','review_body']
df.head(983)


# In[141]:


df.to_json("reviews.json")