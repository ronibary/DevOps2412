from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
dr.get("C:/Ron-Dev/Python-dev/Dev-Ops-Course-241223/DevOps2412/tip_calc 2/tip_calc/index.html")
dr.find_element(By.ID,"billamt").send_keys("100")
dropdown = dr.find_element(By.ID,"serviceQual")
select = Select(dropdown)
select.select_by_value("0.2")
dr.find_element(By.ID,"peopleamt").send_keys("5")
dr.find_element(By.ID,"musicQual").send_keys("5")
dr.find_element(By.ID,"calculate").click()
actual = dr.find_element(By.ID,"tip").text
expected = "9"
assert actual == expected , "The expected tip is not equal to 9"
print(f"Tip was :  {actual}")
sleep(1000)