from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\chromedriver.exe"))


def uni_to_home():
    driver.get('https://www.mbta.com/schedules/28/line?schedule_direction%5Bdirection_id%5D=0&schedule_direction%5Bvariant%5D=28-_-0&schedule_finder%5Bdirection_id%5D=0&schedule_finder%5Borigin%5D=place-rugg')
    approaching = driver.find_element(By.XPATH, '//*[@class="schedule-table__cell schedule-table__cell--time u-nowrap u-bold text-right"]').text
    nextbus = driver.find_element(By.XPATH, '//*[@class="schedule-table__cell schedule-table__cell--time u-nowrap u-bold text-right"]/following::*[@class="schedule-table__cell schedule-table__cell--time u-nowrap u-bold text-right"]').text
    print(approaching)
    print(next_bus)
    
def home_to_uni():
    driver.get('https://www.mbta.com/schedules/28/line?schedule_direction%5Bdirection_id%5D=0&schedule_direction%5Bvariant%5D=28-_-0&schedule_finder%5Bdirection_id%5D=1&schedule_finder%5Borigin%5D=21151')
    approaching = driver.find_element(By.XPATH, '//*[@class="schedule-table__cell schedule-table__cell--time u-nowrap u-bold text-right"]').text
    nextbus = driver.find_element(By.XPATH, '//*[@class="schedule-table__cell schedule-table__cell--time u-nowrap u-bold text-right"]/following::*[@class="schedule-table__cell schedule-table__cell--time u-nowrap u-bold text-right"]').text
    print(approaching)
    print(next_bus)

