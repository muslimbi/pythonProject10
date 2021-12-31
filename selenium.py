from selenium import webdriver

PROXY = "21.65.32.65:3124"

chrome_options = WebDriverWait.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("https://whatismyipaddress.com")