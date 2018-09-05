from selenium import webdriver
import time

getdriver = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Chrome()
driver.get(getdriver)

def Registration(username,password):
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
def click():
    driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    time.sleep(5)
    driver.get("Your Account Links")
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(1)
def follow():
    try:
        for i in range(1, 7500):
            like = driver.find_element_by_css_selector('ul li:nth-of-type({}) button'.format(i)).click()
            unfollow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
            print('Unfollow {} People'.format(i))
            if i==9:
                print('Unfollow {} People'.format(i))

    except:
        print("error Try again")
#Username #password
Registration("Youur_Username","Your_password")
click()
follow()