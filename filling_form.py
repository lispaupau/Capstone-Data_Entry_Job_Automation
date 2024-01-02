import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from get_data import GetData


class Filling:
    def __init__(self):
        self.data = GetData()

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url='https://forms.gle/PvCwGWqKR1P47szx8')
        time.sleep(2)

    def post_data(self):
        for i in range(len(self.data.hrefs_list)):
            addr = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/'
                                                      'div/div[1]/div/div[1]/input')
            addr.send_keys(self.data.addr_list[i])

            price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/'
                                                       'div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(self.data.prices_list[i])

            link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/'
                                                      'div/div[1]/div/div[1]/input')
            link.send_keys(self.data.hrefs_list[i])

            send_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            send_button.click()

            send_more_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            send_more_button.click()
