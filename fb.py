from selenium import webdriver
from getpass import getpass
from bs4 import BeautifulSoup
from hidden import *
import time
# ################################333333333####33333
print ('Give your username and password for facebook')
# username = input('Enter your username: ')
# password = getpass('Enter your password: ')
# ##############################33333333###########3\
# driver = webdriver.Chrome()

driver = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
driver.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=driver)

driver.get('https://www.facebook.com/')
driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(7) # waiting for 7 seconds so that we can load the login page for the data that we want
print (driver.title)

#####################################
driver.find_element_by_class_name('_1vp5').click()
time.sleep(2)
friendsdata = driver.execute_script('return document.documentElement.outerHTML')
###########################################existence

data = BeautifulSoup(friendsdata, 'html.parser')
div1 = data.find('div', attrs={'class': '_5h60', 'id': 'pagelet_timeline_main_column'})
ul = div1.find('ul', attrs={'class': '_6_7 clearfix'})
# print (ul)
li = ul.findAll('li')
# print (li)
for i in range(len(li)):
    # print (i)
    # # print ()
    diva = li[i].find('a', class_ = '_6-6')
    if (diva and i == 2):
        friendslink = diva['href']
print (friendslink)

linkdata = driver.get(friendslink)

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(3)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
time.sleep(2)
alldata = driver.execute_script('return document.documentElement.outerHTML')
# print (alldata)
# driver.quit()

friend = BeautifulSoup(alldata, 'html.parser')
# print (friend)
div7 = friend.find('div', attrs={'class': '_5h60 _30f', 'id': 'pagelet_timeline_medley_friends'})
# print (div7)
div8 = div7.find('div', attrs={'class': '_3i9', 'id': 'collection_wrapper_2356318349'})
# print (div8)
div9 = div8.find('div', attrs={'class': '_5h60 _30f'})
# print (div9)
ul = div9.findAll('ul', class_ = True)
# print (div9)
count = 0
for i in ul:
    # print (i)
    j = i.findAll('li')
    # print (j)
    for k in j:
        ab = k.find('div', class_ = 'clearfix _42ef')
        # print (ab) 
        try:
            cd = ab.find("div", class_="uiProfileBlockContent")
            ef = cd.find('div', class_ = 'fsl fwb fcb')
            gh = ef.find('a')
            print(gh.text)
            count+=1
        except:
            continue
print('Total friends are: ', count)
