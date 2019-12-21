# Facebook-Scraper
In this project, I have scraped the names of all the friends on Facebook after logging in with username and password.

## Requirements

### BeautifulSoup
Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
If you're using Linux based OS, you can install BeautifulSoup using following command in terminal.

`sudo apt-get update && sudo apt-get install python3-bs4` (Python3).

### Selenium Webdriver
Selenium is a software testing framework for the web that facilitates the automation of browsers.
WebDriver is a web automation framework that allows you to execute your tests against different browsers, like Firefox, Chrome .
You can download selenium webdriver using following command in terminal. It will install chromium-chromedriver in your system.

```
sudo apt-get install chromium-chromedriver
```
Or, you can also download appropriate Chrome-Drive for your system. Follow [this link](https://sites.google.com/a/chromium.org/chromedriver/downloads) to know more! If still not working, click [here](https://askubuntu.com/questions/1004947/how-do-i-use-the-chrome-driver-in-ubuntu-16-04) to get the solution from Ask-Ubuntu.

## Instructions to run the Code

Any version of Python3 should be installed on your Linux-based computer. Navigate to your directory where your `fb.py` file is located. You can run the code using the following command on your terminal.

`python3 fb.py`
