from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setup edge driver
options = webdriver.EdgeOptions()

#options.add_argument("user-data-dir=C:/EdgeProfiles/Profile_A") #use different progile

options.add_argument("--start-maximized")
options.add_argument("--inprivate")
driver = webdriver.Edge(options=options)

f2=open("ground_links.txt",'a')




god_link=[] #stores links of interest



def search(keyword,search_bar):
    search_bar.send_keys(Keys.CONTROL, 'a')
    search_bar.send_keys(Keys.BACKSPACE)
    time.sleep(1)  
    search_bar.send_keys(keyword)
    time.sleep(0.5)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(3)

    time.sleep(2)   # small delay, can replace with smarter waits

    # After typing in search bar and waiting for results
    cards = driver.find_elements(By.CSS_SELECTOR, "a[id^='search-click-article-']")

    # print(f"found slips for:{keyword}")


    for card in cards:
        temp=[]
        try:
            link = card.get_attribute("href")
            title = card.find_element(By.CSS_SELECTOR, "span.font-bold").text
            meta = card.find_element(By.CSS_SELECTOR, "span.text-12").text
            # print(f"Title: {title}\nLink: {link}\n")
            sources=int(meta.split()[0]) #error when single digit sources
            if sources<10:
                # print("<10")
                continue
            # print(sources)
            
            # god_link.append(link+'\n')
            f2.write(link+'\n')
        except Exception as e:
            # print("Error extracting card:", e)
            pass
        
    

 
def main():
    driver.delete_all_cookies()

    driver.get("https://ground.news/")
    # time.sleep(10)

    #wait for stage 1 search bar to be clickable
    wait = WebDriverWait(driver, 15)
    search_bar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))
    search_bar.click()


    #wait for stage 2 search bar to be clickable
    search_bar = wait.until(EC.presence_of_element_located((By.ID, "searchfield")))
    
    #opening urls to search from, GDELT
    file=open("urls.txt",'r')

    
    

    urls=file.readlines()
        
    #try for first n urls:
    n=900

    length=len(urls)

    for k in range(900,n): #
        print(k)
        link=urls[k]
        
        driver.delete_all_cookies()

        print(link)
        
        keyword=link.split(sep="/")[::-1]
        # time.sleep(0.5)

        

        # print(keyword)

        if(keyword[0]=="\n"):
            keyword=keyword[1]
        else:
            if '.ece' in keyword[0]:
                keyword=keyword[1]
            else:
                keyword=keyword[0]

        # print(keyword)

        # print(f"for URL: {keyword}")

        
        if n==0:
            break

        search(keyword,search_bar)

        n-=1


if __name__=="__main__":
    main()
    # print(god_link)
    f2.close()
    driver.quit()