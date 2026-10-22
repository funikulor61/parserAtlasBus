from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import csv
from selenium.webdriver.common.keys import Keys
import datetime

MONTHS = {
    'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
    'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12,
}

class parserAB:
    def __init__(self, link, name, surname, phone_number, from_where , where_to, data):
        self.link = link
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.from_where = from_where
        self.where_to = where_to
        self.date = data

    def acceptCoockie(self):
        try:
            clickable_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'cm__btn'))
            )
            clickable_element.click()
            print("Куки успешно приняты.")
            time.sleep(1)
        except TimeoutException:
            print("Элемент '.cm__btn' не найден, продолжаем выполнение кода...")

    def dateToIso(self):
        """'30 октября' -> '2026-10-30'"""
        day, month = self.date.split()                      # '30 октября' -> '30', 'октября'
        m = MONTHS[month.lower()]                           # 'октября' -> 10
        today = datetime.date.today()
        d = datetime.date(today.year, m, int(day))
        if d < today:                                       # эта дата уже прошла? -> следующий год
            d = datetime.date(today.year + 1, m, int(day))
        return d.isoformat()

    def openBus(self):
        url = (f'https://atlasbus.by/Маршруты/{self.from_where}/{self.where_to}'
               f'?date={self.dateToIso()}&passengers=1')
        self.driver.get(url)
        self.acceptCoockie()
        time.sleep(3)