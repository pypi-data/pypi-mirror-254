
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager            #for ChromeDriver installation
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService


import sys, json
import urllib.request
sys.path.append("..") # Adds higher directory to python modules path

from helper import requestheader
from core import mdr

from loguru import logger

import time, os, re, pickle
from pathlib import Path
import keyring as kr
import getpass

logger.add(f"./logs/{__name__}.log",mode="w", backtrace=True, diagnose=True, level="DEBUG", filter="Login")
#logger.add(sys.stdout, backtrace=True, diagnose=True)
dbgPrint = logger
class Login(object):
    """description of class"""
    def __init__(self):
        pass

    def delete_session(self):
        session_path = os.path.abspath(os.path.dirname(__file__)) + "\..\session"
        for p in Path(session_path).glob("mdr.pkl"):
            os.remove(p)

    def wait(self, driver, timeout, type, element):
        while True:
            try:
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((type, element)))
                break
            except TimeoutException:
                dbgPrint.warning("[-] Loading took too much time!!!")
        dbgPrint.debug("[+] Your webpage is ready...")


    def create_driver(self):
        try:
            service = ChromeService(ChromeDriverManager().install())
        except ValueError:
            latest_chromedriver_version_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
            latest_chromedriver_version = urllib.request.urlopen(latest_chromedriver_version_url).read().decode('utf-8')
            service = ChromeService(ChromeDriverManager(version=latest_chromedriver_version).install())
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-logging')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])          #Disable logging of webdriver
                                                                                        #Fixed for failed driver update
                                                                                        #pip install --upgrade webdriver-manager
        driver = webdriver.Chrome(service=service, options=options)                     #August 26, 2023
#        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version="114.0.5735.90").install()), options=options)  #New update 8/15/2023 11:35:31 PM
        return driver


    def webapp_snypr(self, driver, web_app=None):
        override = False
        one_time_code = ""

        while len(one_time_code) <= 8:
            try:
                one_time_code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder=' One-Time Passcode']"))).get_attribute("value")
            except:
                if "mss-sso.verizonbusiness.com/csso/#/error" in driver.current_url:
                    dbgPrint.debug("Need to restart")
                    return False
                elif "mss-sso.verizonbusiness.com/csso/?goto" not in driver.current_url:
#                    dbgPrint.debug("[+] Button override")
                    break
            if len(one_time_code) == 8:
                driver.find_element(By.XPATH, "//input[@type='submit']").click()
        return True


    def setup(self):
        if kr.get_password('snypr', "username"):
            return
        dbgPrint.debug("Setup your username and password for MDR portal...")
        username = input("Enter your username: ")
        while(1):
            password = getpass.getpass("Enter your password: ")            
            if password == getpass.getpass("Verify your password: "):
                dbgPrint.debug("Successful")
                break
            else:
                dbgPrint.debug("Unmatched")
    
        kr.set_password('snypr', "username", username)
        kr.set_password('snypr', username, password)
        dbgPrint.debug("Setup successful!")

    def delete_credentials(self):
        username = kr.get_password('sypr', "username")
        try:
            kr.delete_password('snypr', "username")
            kr.delete_password('snypr', username)
        except kr.errors.PasswordDeleteError:
            dbgPrint.error("Credentials cleared")

    def snyper(self):           #Return cookie
        
        cookie = ""
        username = kr.get_password('snypr', "username")
        password = kr.get_password('snypr', username)

        mdr_page = "https://mss-24.verizonbusiness.com/unified/#/dashboard/executive-summary"
        if not hasattr(self, "driver"):
            self.driver = self.create_driver()
        dbgPrint.info("[+] Checking session...")
        self.driver.get(mdr_page)
        self.wait(self.driver, 10, By.XPATH, "//*[@id='username']")
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(username)
        self.wait(self.driver, 10, By.XPATH, "//input[@type='button' and @value='Continue']")
        self.driver.find_element(By.XPATH, "//input[@type='button' and @value='Continue']").click()
        self.wait(self.driver, 10, By.XPATH, "//input[@id='password']")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.wait(self.driver, 10, By.XPATH, "//input[@type='button' and @value='Sign in']")
        self.driver.find_element(By.XPATH, "//input[@type='button' and @value='Sign in']").click()

        if not self.webapp_snypr(self.driver):
            cookie = self.snyper()
        if cookie:
            return cookie
        self.wait(self.driver, 10, By.XPATH, "//div[@class='Go_To_MDR_Portal']/a")

        target = self.driver.find_element( By.XPATH, "//div[@class='Go_To_MDR_Portal']/a").get_property("href")

        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles)-1])
        self.driver.get(target)
        time.sleep(5)
        
        groovy_rails = requestheader.RequestHeader(self.driver, "org.codehaus.groovy.grails.SYNCHRONIZER_TOKEN")
        cookie = {i.split("=")[0].strip(" "):i.split("=")[1] for i in list([i for i in groovy_rails.headers._headers if i[0] == "cookie"][0])[1].split(";")}

        return cookie