from selenium import webdriver
import time


browser = webdriver.Chrome()
time.sleep(2)
browser.execute_script('document.title="Script executing";')
browser.execute_script("alert('Robots at work');")

time.sleep(2)