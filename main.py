from selenium import webdriver


#  webdriver instructs the behaviour of our browser
def get_driver():
  # Set options to make Web browsing easier
  print("******************88")
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  print("******************88")
  driver = webdriver.Chrome(options=options)
  print("******************88")
  driver.get("https://automated.pythonanywhere.com/")

  return driver


def main():
  driver = get_driver()
  element = driver.find_element(by="xpath",
                                value="/html/body/div[1]/div/h1[1]")
  return element.text


print(main())
