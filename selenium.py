Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import selenium
>>> from selenium import webdriver
>>> driver = webdriver.Firefox()
>>> driver.get(https://www.google.co.in/webhp?ie=utf-8&oe=utf-8&gws_rd=cr&ei=UbcCV8eJH4a4uATHkLvgDQ)
SyntaxError: invalid syntax
>>> driver.get("https://www.google.co.in/webhp?ie=utf-8&oe=utf-8&gws_rd=cr&ei=UbcCV8eJH4a4uATHkLvgDQ")
>>> driver.get("http://cpcb.nic.in/agra_data.php")
posts = driver.find_elements_by

>>> driver.get("http://cpcb.nic.in/agra_data.php")
posts = driver.find_elements_by_class_name("href")
>>> for post in posts:
	print (post.text)

	

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for post in posts:
NameError: name 'posts' is not defined
>>> 
>>> 

>>> driver.find_element_by_html("<a href="AGRADATA/01.02.16T.pdf" target="_blank">01.02.2016</a>").click()
SyntaxError: invalid syntax
>>> driver.find_element_by_html("""<a href="AGRADATA/01.02.16T.pdf" target="_blank">01.02.2016</a>""").click()

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    driver.find_element_by_html("""<a href="AGRADATA/01.02.16T.pdf" target="_blank">01.02.2016</a>""").click()
AttributeError: 'WebDriver' object has no attribute 'find_element_by_html'
>>> 
>>> driver.find_element_by_xpath("""/html/body/table/tbody/tr[9]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[3]/td/table/tbody/tr[12]/td[1]/div/a""").click()
>>> posts = driver.find_elements_by_xpath("""/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[51]""")
>>> for post in posts:
	print (post.text)

	
>>> 
>>> driver = webdriver.Firefox()
>>>  driver.get("http://cpcb.nic.in/agra_data.php")
 
  File "<pyshell#23>", line 2
    driver.get("http://cpcb.nic.in/agra_data.php")
    ^
IndentationError: unexpected indent
>>> driver.get("http://cpcb.nic.in/agra_data.php")
>>> driver.find_element_by_xpath("""/html/body/table/tbody/tr[9]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[3]/td/table/tbody/tr[12]/td[1]/div/a""").click()
>>> posts = driver.find_elements_by_attribute_name("style")

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    posts = driver.find_elements_by_attribute_name("style")
AttributeError: 'WebDriver' object has no attribute 'find_elements_by_attribute_name'
>>>  posts = driver.find_elements_by_name("style")
 
  File "<pyshell#27>", line 2
    posts = driver.find_elements_by_name("style")
    ^
IndentationError: unexpected indent
>>> posts = driver.find_elements_by_name("style")
>>> for post in posts:
	print (post.text)

	
>>> 
