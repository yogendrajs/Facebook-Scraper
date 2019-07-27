from selenium import webdriver
from getpass import getpass # to hide password while entering
from bs4 import BeautifulSoup
from os import path
import time, os, json, pprint
#########################33
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
driver.find_element_by_xpath("//input[@type='submit']").click() # clicking on the login button

time.sleep(5) # waiting for 5 seconds so that we can load the HOME page for the data that we want
print (driver.title) # It gives the required title of the page

#####################################
# from here onwards, I'm finding elements 
driver.find_element_by_class_name('_1vp5').click()
time.sleep(3)
###########################################existence
driver.find_element_by_xpath('//a[@data-tab-key="friends"]').click() # to click on Friends button
time.sleep(2)
name = driver.find_element_by_xpath('//*[@id="fb-timeline-cover-name"]/a').text
print ("Your Full name is: ", name.split('\n')[0])
name = name.split('\n')[0]

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

# driver.quit()

# from here, I am starting the parsing of the friends data, so that we could get all the friends name and their count
friend = BeautifulSoup(alldata, 'html.parser')
# print (friend)
div7 = friend.find('div', attrs={'class': '_5h60 _30f', 'id': 'pagelet_timeline_medley_friends'})
# print (div7)
div8 = div7.find('div', attrs={'class': '_3i9', 'id': 'collection_wrapper_2356318349'})

time.sleep(2.5)
ul = div8.findAll('ul')
# print (div9)
count = 0
exists = path.exists(os.getcwd() + '/fb.json') # to get into the present directory where this json file locates

dic = {}
friendlist = []
print ('\nYour Friends-List is: ')
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
            friendName = gh.text # It will print all the names of the friends after scrolling and loading the whole page 
            friendlist.append(friendName)
            count+=1
        except:
            continue

dic['name'] = name # name of the owner of the facebook id
dic['friends'] = friendlist # friendslist of the owner person in a list
dic['total'] = count # total number of friends
pprint.pprint(dic)
# caching of the data in the local json file
if not exists:
    with open (os.getcwd() + '/fb.json', 'w') as file:
        # if (os.path.getsize(os.getcwd() + '/fb.json') == 0):
        file.write(json.dumps([]))
        file.close()
with open(os.getcwd() + '/fb.json', 'r+') as content:
    data = json.loads(content.read())
    for i in data:
        if i['name'] == name:
            i['friends'] = friendlist
            break
    else:
        data.append(dic)
    content.close()
with open(os.getcwd() + '/fb.json', 'w') as files:
    files.write(json.dumps(data, indent=4, sort_keys=False))

print('Total friends are: ', count) # It will tell you how many friends do you have. May differ with those that have been shown there. But it counts the original total one.
