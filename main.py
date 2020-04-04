"""
#browser.get("https://www.instagram.com/p/B-NfqY7nIUL/");  # cok
#browser.get("https://www.instagram.com/p/B-FX2zxJuuh/");  # cok
browser.get("https://www.instagram.com/p/B-NO0LJnKmG/")  # az
#browser.get("https://www.instagram.com/p/B-B80jcHE61/")  # az
print(json.dumps(users))
print("")
print(comments)
browser.quit()"""
import sys
import logging
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import json
import time
    


try:
    
    #Log Vars
    log_file = "instagrambot.log"
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    
    
    
    #General Vars
    debug = False
    error_trace = False
    
    base_url = "https://www.instagram.com/p/B-NfqY7nIUL/"
    sub_url = ""

    
    
    #Objects
    browser = None
    


    #Fonctions    
    def write_log(l, s):#l => 1: info, 2:warning, 3:error
        global debug
        
        logger.info('%s', str(s))
        
        if debug:
            print("LOG -> level:" + str(l) + " - " + str(s))
            
    def args_control():
        if len(sys.argv) != 2:
            write_log(2, "Args invalid" + str(sys.argv))
            sys.exit(1)
            
        write_log(1, "Args OK")
            
    def fill_vars():
        global browser, sub_url
        sub_url = sys.argv[1]        
        browser = get_browser()
        
        write_log(1, "Vars filled")

    def get_browser():
        global debug
        
        if debug:
            temp = webdriver.Chrome("chromedriver.exe")   
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            temp = webdriver.Chrome("chromedriver.exe", options=options)
              
        write_log(1, "Browser created")        
        return temp
    
    def go_to_page(url):
        global browser
        browser.get(url)
        write_log(1, "Go url: " + url)
        
    def go_to_media_file():
        global base_url, sub_url
        go_to_page(base_url+sub_url)
        
    def fill_all_comments_on_page():
        global browser
        
        try:
            while True:
                WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, "dCJp8")))
                more = browser.find_element_by_class_name("dCJp8")
                more.click()
        except Exception as e:
            temp = True
        
    def get_data_from_page():
        data = []
        user_uls = browser.find_elements_by_xpath('//ul[contains(@class,"Mr508")]')
        for user_ul in user_uls:
            username = user_ul.find_element_by_xpath('.//h3//a').text
            comment = user_ul.find_element_by_xpath('.//div[@class="C4VMK"]//span').text
             
            temp = {"username": username, "comment": comment}
            data.append(temp)
            
        return data
        
    def get_data():
        go_to_media_file()
        fill_all_comments_on_page()
        data = get_data_from_page()
        
        close_browser()
        
        return data
        
    def print_data(data):
        temp = {"status": "OK", "data": data}
        print(json.dumps(temp))
    
    def close_browser():
        global browser    
        browser.quit()
        
        write_log(1, "Browser closed")
    
    def main():
        args_control()
        fill_vars()
        
        data = get_data()
        
        print_data(data)
    

    #Main
    if __name__ == "__main__":
        write_log(1, "Started")        
        main()


    
except SystemExit as e:
    sys.exit(e)
    
except Exception as e:
    try:
        write_log(3, "Error handled")
    except Exception as ee:
        def write_log(l, s):
            m = "Level: " + str(l) + " - " + str(s)
            print(m)
            with open(log_file, "a") as f:
                f.write(m)
                
        write_log(3, "Error handled")
    
    exc_type, exc_obj, exc_tb = sys.exc_info()    
    write_log(3, "General error! " + str(e) + " (line: " + str(exc_tb.tb_lineno) + ")")
    
    if error_trace:
        print(traceback.print_exc())