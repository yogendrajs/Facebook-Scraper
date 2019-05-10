from selenium import webdriver
from getpass import getpass # to hide password while entering
from bs4 import BeautifulSoup
import time

print ('Give your username and password for facebook')
username = input('Enter your username: ')
password = getpass('Enter your password: ') # here we're hiding password while entering using getpass
# ##############################33333333###########3\

driver = webdriver.ChromeOptions() # initializing driver
prefs = {"profile.default_content_setting_values.notifications" : 2} # to hide browser notifications
driver.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=driver)

driver.get('https://www.facebook.com/') # requesting to this link
driver.find_element_by_xpath('//*[@id="email"]').send_keys(username) # sending facebook id username
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password) # sending facebook id password
driver.find_element_by_xpath("//input[@type='submit']").click() # clicking on the submit button

time.sleep(7) # waiting for 7 seconds so that we can load the HOME page for the data that we want
print (driver.title) # It gives the required title of the page

#####################################
# from here onwards, I'm finding elements 
driver.find_element_by_class_name('_1vp5').click()
time.sleep(2)
friendsdata = driver.execute_script('return document.documentElement.outerHTML')
###########################################existence

# started parsing for FRIENDS's link so that we can request on that link to get the html of friends data 
data = BeautifulSoup(friendsdata, 'html.parser')
div1 = data.find('div', attrs={'class': '_5h60', 'id': 'pagelet_timeline_main_column'})
div2 = div1.find('div', attrs={'class': '_5h60', 'id': 'timeline_top_section'})
div3 = div2.find('div', attrs={'class': 'fbTimelineSection fbTimelineTopSection', 'id': None})
div4 = div3.find('div', attrs={'class': 'drop_elem', 'id': 'fbProfileCover'})
div5 = div4.find('div', attrs={'class': 'clearfix', 'id': 'fbTimelineHeadline'})
div6 = div5.find('div', attrs={'class': '_70k', 'id': None})
ul = div1.find('ul', attrs={'class': '_6_7 clearfix', 'id': True})
# print (ul)
li = ul.findAll('li')
# print (li)
for i in range(len(li)):
    diva = li[i].find('a', class_ = '_6-6')
    if (diva and i == 2):
        friendslink = diva['href']
        break
print ('Friends Link: ', friendslink) # required link of friends section

linkdata = driver.get(friendslink) # requesting to the friends link

# starting scrolling the whole page till it loads all the friends and reach the end of the page
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

# from here, I am starting the parsing of the friends data, so that we could get all the friends name and their count
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
print ('Your Friends-List is: \n')
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
            print(gh.text) # It will print all the names of the friends after scrolling and loading the whole page 
            count+=1
        except:
            continue
print('Total friends are: ', count) # It will tell you how many friends do you have. May differ with those that have been shown there. But it counts the original total one.
