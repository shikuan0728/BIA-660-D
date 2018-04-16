import requests
import bs4

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



