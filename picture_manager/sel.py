from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def sel():
    print("test")
    browser = webdriver.Chrome("C:/Users/Jeremy/Downloads/chromedriver_win32/chromedriver.exe")
    browser.get('https://portal.zakeke.com/en-US/Admin/Login')
    time.sleep(2)
    browser.find_element_by_id("txt-username").click()
    browser.find_element_by_id("txt-username").send_keys(os.getenv("ZAKEKE_USER"))
    browser.find_element_by_id("txt-password").click()
    browser.find_element_by_id("txt-password").send_keys(os.getenv("ZAKEKE_PW"))
    browser.find_element_by_id("btn-submit").click()
    browser.get('https://portal.zakeke.com/en/Admin/Images')
    time.sleep(3)
    browser.find_element_by_id("btn-add-images").click()
    time.sleep(3)
    browser.execute_script("document.getElementsByName('file')[0].style.display='block';")
    browser.execute_script("document.getElementsByName('file')[0].style.position='center';")
    browser.find_element_by_name("file").send_keys("C:\\Users\\Jeremy\\Downloads\\1.png")
    time.sleep(3)
    browser.execute_script("document.getElementsByClassName('selectpicker')[0].style.display='block';")
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="dialogs-portal"]/div/div/div[1]/div[1]/div/select/option[1]').click()
    time.sleep(2)
    #browser.find_element_by_class_name('modal-footer text-center').click()
    browser.find_element_by_xpath('/html/body/div[28]/ul/li[2]').click()
    browser.find_element_by_xpath('/html/body/div[28]/ul/li[2]').click()
    browser.find_element_by_xpath('//*[@id="dialogs-portal"]/div/div/div[2]/button').click()
    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="images-page"]/div/div[2]/ul/li/div/div[2]/ul/li[2]/a/i').click()


    time.sleep(3)

    #browser.findElement(By.xpath("//button[text()='UPLOAD IMAGE']")).click();
    time.sleep(20)


if __name__ == '__main__':
    sel()