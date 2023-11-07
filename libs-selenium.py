# Dokümantasyon: https://selenium-python.readthedocs.io/index.html
# gecko driver kuruldu - firefox
from selenium import webdriver

driver = webdriver.Firefox()

url = "https://egoistpizza.github.io"

driver.get(url)
