import SeleniumChrome
from SeleniumChrome import *

print(SeleniumChrome.__version__)

driver = SeleniumChrome(keep_alive=True)
driver.get("https://www.google.com")
