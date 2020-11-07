from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

def get_mileage_popup_selector(n): # 0 to 14
    return '#row' + str(n) + 'jqxgrid > div:nth-child(7) > span > a:nth-child(4) > img'

def get_syllabus_popup_selector(n):
    return '#row' + str(n) + 'jqxgrid > div:nth-child(7) > span > a:nth-child(3) > img'


CURRI_LINK = 'http://ysweb.yonsei.ac.kr:8888/curri120601/curri_new.jsp#top'
class_info_title = ['학정번호', '과목명', '학점', '담당교수', '강의시간', '강의실', '정원', '참여인원', '전공자정원', '1학년정원', '2학년정원', '3학년정원', '4학년정원', '교환가능여부', '최대마일리지', '최소값', '최대값', '평균값']
mileage_rank_title = ['순위', '마일리지', '전공자여부', '신청과목수', '졸업신청', '초수강여부', '총이수/졸업이수', '직전학기이수/학기당수강', '학년', '수강여부', '비고']
year_list = ['2019', '2020']
semester_list = ['1학기', '2학기']

search_selector = '#myForm > table > tbody > tr:nth-child(1) > td:nth-child(1) > a:nth-child(6) > img'
category1_selector = '#OCODE1'
category2_selector = '#S2'
year_selector = '#HY'
semester_selector = '#HG'
pageinfo_selector = '#pager > div > div > div:nth-child(3)'
nextpage_selector = '/html/body/div[5]/form[2]/table/tbody/tr[3]/td/div/div[2]/div/div[8]/div/div/div[2]/div'

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")

driver = webdriver.Chrome('C:\chromedriver')
# driver = webdriver.Chrome('C:\chromedriver', chrome_options=options)
driver.get(CURRI_LINK)
SELECTOR = driver.find_element_by_css_selector
SELECTOR_XPATH = driver.find_element_by_xpath
SEARCH_CLICK = SELECTOR(search_selector).click

def switch_window(n):
    driver.switch_to_window(driver.window_handles[n])

print('get_driver_for_crawling imported')
