# %%

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import re


geckodriver_path = "/snap/bin/geckodriver"
driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)

firefox_options = Options()
firefox_options.set_preference('security.tls.version.min', 1)
browser = webdriver.Firefox(service=driver_service, options=firefox_options)

# %%
browser.get("https://aloe.anfdf.ro/")

# %%
# Login
username = browser.find_element(By.XPATH, "//input[@name='user']")
password = browser.find_element(By.XPATH, "//input[@name='pass']")
login = browser.find_element(By.XPATH, "//input[@name='LOGIN']")

username.send_keys("guest")
password.send_keys("guest")
login.click()

# %%
# Go to Codex
codex = browser.find_element(By.LINK_TEXT, 'Căutare')
codex.click()

# %%
all_months = browser.find_element(By.XPATH, "//input[@name='lunaall']")
all_years = browser.find_element(By.XPATH, "//input[@name='aniall']")

all_months.click()
all_years.click()

# %%
# Search
search_bar = browser.find_element(By.XPATH, "//select[@name='cautare']")
select = Select(search_bar)

# PRODUS = 1
select.select_by_value('1')

submit_button = browser.find_element(By.XPATH, "//input[@name='b13']")
submit_button.click()

#%%
main_table = browser.find_element(By.XPATH, "//table[1]")
products = main_table.find_elements(By.CLASS_NAME, "HeaderMenuLink2slim")

product_ids = []
for product in products:
    onclick = product.get_attribute("onclick")
    match = re.search(r"(\d+)", onclick)
    product_ids.append(match.group(1))


for id in product_ids:
    URL = f"https://aloe.anfdf.ro/index.php?id={id}&type=product"



# %%
