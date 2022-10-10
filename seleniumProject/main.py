from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

EMAIL = 'johnabruzzi123@mail.com'
PASSWORD = 'michaelscofield1'
URL = 'https://www.linkedin.com/login'
JOB_SEARCH = 'data analyst'

all_job_ids = set()
all_job_urls = set()

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
PATH = "C:/Users/user/PycharmProjects/seleniumProject/chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH,chrome_options=opts)

driver.get(URL)

email_object = driver.find_element(By.ID , 'username')
email_object.send_keys(EMAIL)

password_object = driver.find_element(By.ID , 'password')
password_object.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.CLASS_NAME , 'btn__primary--large')
sign_in_button.click()

driver.get('https://www.linkedin.com/jobs/search/?keywords=data%20analyst&refresh=true')

def get_job_ids():
    job_ids_string_list = re.findall('data-job-id=".*"',driver.page_source)
    job_ids = []
    for job_id_string in job_ids_string_list:
        job_ids.append(job_id_string[13:23])
    return job_ids

for i in range(20):
    driver.get('https://www.linkedin.com/jobs/search/?currentJobId=' + get_job_ids()[-1] + '&keywords=data%20analyst&start=' + str(8*i))
    for elem in get_job_ids():
        all_job_ids.add(elem)

for job_id in all_job_ids:
    driver.get('https://www.linkedin.com/jobs/search/?currentJobId=' + job_id + '&keywords=data%20analyst')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'jobs-apply-button')))
        apply_button = driver.find_elements(By.CLASS_NAME, 'jobs-apply-button')
        apply_button[0].click()
        driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL + Keys.TAB)
        all_job_urls.add(driver.current_url)
        driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL + Keys.TAB + Keys.SHIFT)
    except:
        pass
    finally:
        pass

print(all_job_urls)


