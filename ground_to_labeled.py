from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

f1=open("ground_links.txt",'r')

f2=open("main_labeled_data.csv","a")

ground_links=f1.readlines()

# print(ground_links)


options = webdriver.EdgeOptions()

# options.add_argument("user-data-dir=C:/EdgeProfiles/Profile_B") #use different profile
options.add_argument("--inprivate")
options.add_argument("--start-maximized")
driver = webdriver.Edge(options=options)


file_len=len(ground_links)

n=1700

for i in range(1500,n):
    print(f'---##{i}##---')
    driver.delete_all_cookies()
    time.sleep(0.5)
    # print("2")
    driver.get(ground_links[i])
    # print("3")
    time.sleep(2)
    try:
        driver.find_element(By.ID, "more-stories").click()
        time.sleep(1)
    except:
        pass
    # print()
    # print("4")
 

    summaries = driver.find_elements(By.CSS_SELECTOR, "div#article-summary")  # multiple, despite 'id'

    rows = []
    for box in summaries:
        try:
            # Bias text (e.g., "Lean Left", "Right", "Lean Right")
            bias_el = box.find_element(By.CSS_SELECTOR, "a[id^='article-source-bias-'] div")
            bias_text = bias_el.text.strip()

            print(bias_text)

            # External URL: take the <a> that wraps the <h4> title

            title_link = box.find_element(By.CSS_SELECTOR, "a[target='_blank'] h4")
            ext_a = title_link.find_element(By.XPATH, "./..")  # parent <a>
            url = ext_a.get_attribute("href")

            outlet = box.find_element(By.CSS_SELECTOR, "a[id^='article-source-info-'] span").text.strip()
            
            f2.write(outlet+' @ '+bias_text+' @ '+url+'\n')
        except:
            continue

    time.sleep(2)


driver.quit()
