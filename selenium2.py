
import selenium
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://cpcb.nic.in/agra_data.php")
driver.find_element_by_xpath("""/html/body/table/tbody/tr[9]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[3]/td/table/tbody/tr[12]/td[1]/div/a""").click()
posts = driver.find_elements_by_xpath("""/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[51]""")
for post in posts:
	print (post.text)


##def paste_keys(self, xpath, text):
##    os.system("echo %s| clip" % text.strip())
##    el = self.driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[51]""")
##    el.send_keys(Keys.CONTROL, 'v')
