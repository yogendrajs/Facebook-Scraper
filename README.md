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
You can download selenium webdriver using following commands in terminal.

`wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip`.

`unzip chromedriver_linux64.zip`.

Now, execute the following commands to configure ChromeDriver on your system.

`sudo mv chromedriver /usr/bin/chromedriver`.

`sudo chown root:root /usr/bin/chromedriver`.

`sudo chmod +x /usr/bin/chromedriver`.

The Selenium Server is required to run Remote Selenium WebDrivers. You need to download the Selenium standalone server jar file using the below commands or visit here to find the latest version of Jar file.

`wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar`.

## Instructions to run the Code

Any version of Python3 should be installed on your Linux-based computer. Navigate to your directory where your `fb.py` file is located. You can run the code using the following command on your terminal.

`python3 fb.py`
