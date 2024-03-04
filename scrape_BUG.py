from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

url = "https://www.idnfinancials.com/id/byan/pt-bayan-resources-tbk#managements"

driver = None

try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    info_elements = driver.find_elements(By.CLASS_NAME, 'info')

    data = []
    for info in info_elements:
        try:
            name_element = info.find_element(By.CLASS_NAME, 'name')
            title_element = info.find_element(By.CLASS_NAME, 'title')
            # Lanjutkan dengan mengumpulkan data
        except NoSuchElementException as e:
            print("Elemen tidak ditemukan. Lanjutkan ke elemen berikutnya.")
            print("Error occurred at line:", e.__traceback__.tb_lineno)

        if name_element and title_element:
            no = len(data) + 1
            data.append({
                'no': str(no),
                'name': name_element.text,
                'title': title_element.text
            })

    with open('output.csv', mode='w', newline='') as file:
        fieldnames = ['no', 'name', 'title']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)
except Exception as e:
    print("This is the error: ", e)
    print("Error occurred at line:", e.__traceback__.tb_lineno)
finally:
    if driver:
        driver.quit()