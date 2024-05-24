from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_product_json(browser, url):
    # %%
    product_json = {
        "details": {},
        "active_substances": {},
        "risk_and_security": {},
        "usages": {},
        "mrl": {}
    }

    browser.get(url)
    main_table = browser.find_element(By.XPATH, "//table[1]")
    product_table = main_table.find_element(By.XPATH, ".//table[2]")

    # %%
    # Details
    details = {}
    details_table = product_table.find_element(By.XPATH, ".//table[1]")
    tr_elements = details_table.find_elements(By.TAG_NAME, "tr")
    for tr in tr_elements:
        try:
            name = tr.find_element(By.XPATH, ".//td[1]").text.replace(":", "").strip()
            value = tr.find_element(By.XPATH, ".//td[2]").text.strip()
            details[name] = value
        except NoSuchElementException:
            continue

    product_json["details"] = details
    # print(details)

    # %%
    # Active substances
    active_substances = {}
    active_substances_table = product_table.find_element(By.XPATH, ".//table[2]")
    tr_elements = active_substances_table.find_elements(By.TAG_NAME, "tr")

    header = tr_elements[1] if tr_elements else None
    if header:
        h1 = header.find_element(By.XPATH, ".//td[1]").text
        h2 = header.find_element(By.XPATH, ".//td[2]").text
        h3 = header.find_element(By.XPATH, ".//td[3]").text

        for idx, tr in enumerate(tr_elements[2:]):
            try:
                substance_name = tr.find_element(By.XPATH, ".//td[1]").text
                value = tr.find_element(By.XPATH, ".//td[2]").text
                um = tr.find_element(By.XPATH, ".//td[3]").text
                active_substances[str(idx)] = {
                    h1: substance_name,
                    h2: value,
                    h3: um
                }
            except NoSuchElementException:
                continue

        product_json["active_substances"] = active_substances
        # print(active_substances)

    # %%
    # Risk and security
    risk_and_security = {}
    risk_and_security_table = product_table.find_element(By.XPATH, ".//table[3]")
    tr_elements = risk_and_security_table.find_elements(By.TAG_NAME, "tr")

    header = tr_elements[1] if tr_elements else None
    if header:
        h1 = header.find_element(By.XPATH, ".//td[1]").text
        h2 = header.find_element(By.XPATH, ".//td[2]").text

        for idx, tr in enumerate(tr_elements[2:]):
            try:
                phrase = tr.find_element(By.XPATH, ".//td[1]").text
                category = tr.find_element(By.XPATH, ".//td[2]").text
                risk_and_security[str(idx)] = {
                    h1: phrase,
                    h2: category
                }
            except NoSuchElementException:
                continue

        product_json["risk_and_security"] = risk_and_security
        # print(risk_and_security)

    # %%
    # Usages
    usages = {}
    usages_table = product_table.find_element(By.XPATH, ".//table[4]")
    tr_elements = usages_table.find_elements(By.TAG_NAME, "tr")

    header = tr_elements[1] if tr_elements else None
    if header:
        h1 = header.find_element(By.XPATH, ".//td[1]").text
        h2 = header.find_element(By.XPATH, ".//td[2]").text
        h3 = header.find_element(By.XPATH, ".//td[3]").text
        h4 = header.find_element(By.XPATH, ".//td[4]").text
        h5 = header.find_element(By.XPATH, ".//td[5]").text
        h6 = header.find_element(By.XPATH, ".//td[6]").text

        for (idx, tr) in enumerate(tr_elements[2:]):
            try:
                crop = tr.find_element(By.XPATH, ".//td[1]").text
                harmful_agent = tr.find_element(By.XPATH, ".//td[2]").text
                name = tr.find_element(By.XPATH, ".//td[3]").text
                dose = tr.find_element(By.XPATH, ".//td[4]").text
                waiting_time = tr.find_element(By.XPATH, ".//td[5]").text
                no_treatments = tr.find_element(By.XPATH, ".//td[6]").text

                usages[str(idx)] = {
                    h1: crop,
                    h2: harmful_agent,
                    h3: name,
                    h4: dose,
                    h5: waiting_time,
                    h6: no_treatments
                }
            except NoSuchElementException:
                continue

        product_json["usages"] = usages
        # print(usages)

    # %%
    # MRL
    mrl = {}
    mrl_table = product_table.find_element(By.XPATH, ".//table[5]")
    tr_elements = mrl_table.find_elements(By.TAG_NAME, "tr")

    header = tr_elements[1] if tr_elements else None
    if header:
        h1 = header.find_element(By.XPATH, ".//td[1]").text
        h2 = header.find_element(By.XPATH, ".//td[2]").text
        h3 = header.find_element(By.XPATH, ".//td[3]").text
        for idx, tr in enumerate(tr_elements[2:]):
            try:
                residues = tr.find_element(By.XPATH, ".//td[1]").text
                vegetable_product = tr.find_element(By.XPATH, ".//td[2]").text
                mrl = tr.find_element(By.XPATH, ".//td[3]").text
                mrl[str(idx)] = {
                    h1: residues,
                    h2: vegetable_product,
                    h3: mrl
                }
            except NoSuchElementException:
                continue

        product_json["mrl"] = mrl
        # print(mrl)

    return product_json
# %%
