# %%
import json
import re
import time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from utils import get_product_json

geckodriver_path = "/snap/bin/geckodriver"
driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)

firefox_options = Options()
firefox_options.set_preference('security.tls.version.min', 1)
browser = webdriver.Firefox(service=driver_service, options=firefox_options)

# Wait up to 10 seconds for the element to be loaded
wait = WebDriverWait(browser, 3)

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
# Search
all_months = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='lunaall']")))
all_years = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='aniall']")))
all_months.click()
all_years.click()
search_bar = browser.find_element(By.XPATH, "//select[@name='cautare']")
select = Select(search_bar)

# PRODUS = 1
select.select_by_value('1')
submit_button = browser.find_element(By.XPATH, "//input[@name='b13']")
submit_button.click()

# %%
# Get product IDs
main_table = browser.find_element(By.XPATH, "//table[1]")
products = main_table.find_elements(By.CLASS_NAME, "HeaderMenuLink2slim")

product_ids = []
for product in products:
    onclick = product.get_attribute("onclick")
    match = re.search(r"(\d+)", onclick)
    product_ids.append(match.group(1))

# %%
# Scrape product pages
products_json = {}
for product_id in product_ids:
    URL = f"https://aloe.anfdf.ro/index.php?id={product_id}&type=product"
    product_json = get_product_json(browser, URL)
    products_json[product_id] = product_json
    print(f"Product {product_id}..................DONE")
    time.sleep(0.1)

# %%
# Save JSON
current_date = datetime.now().date()
current_iso_date = current_date.isoformat().replace("-", "")

with open(f"{current_iso_date}-codex.json", "w", encoding='utf-8') as fd:
    json.dump(products_json, fd)
