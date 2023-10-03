import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.airbnb.com/rooms/51046236"

driver = webdriver.Chrome()

driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_1foj6yps')))

driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.CLASS_NAME, '_1foj6yps'))

time.sleep(5)

booked_dates = driver.find_elements(By.XPATH, '//td[.//@data-is-day-blocked="true"]')
filtered_dates = [date.get_attribute('aria-label') for date in booked_dates if 'Unavailable' in date.get_attribute('aria-label')]

for date in filtered_dates:
    print(date.split('.')[0])

driver.quit()
