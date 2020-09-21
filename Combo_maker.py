from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import sys
import time



service = Service('/usr/bin/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
#options.add_argument("--headless")
driver=webdriver.Chrome(chrome_options=options, service = service)

#driver=webdriver.Chrome(options = chrome_options, service = service)


with open("desc.txt","w") as file:
	file.write("Starting")

def writer(line):
	with open("desc.txt","a") as file:
		file.write(str(line)+"\n")

def desc_ext(link):
	driver.get(link)
	#desc = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[6]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/div/div")
	#wait = 
	time.sleep(2)
	desc = [my_href.text for my_href in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[6]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/div/div")))]

	writer(desc)

def main(link):

	
	driver.get(link)
	link_lt = [my_href.get_attribute("href") for my_href in WebDriverWait(driver, 	5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))]

	return link_lt





linkss = ["https://www.youtube.com/results?search_query=hotstar+accounts&sp=EgIIAg%253D%253D","https://www.youtube.com/results?search_query=hotstar+accounts+free&sp=EgIIAg%253D%253D","https://www.youtube.com/results?search_query=hotstar+premium+accounts&sp=EgIIAg%253D%253D","https://www.youtube.com/results?search_query=hotstar+ipl+accounts&sp=EgIIAg%253D%253D","https://www.youtube.com/results?search_query=hotstar+account+new&sp=EgIIAg%253D%253D""https://www.youtube.com/results?search_query=hotstar+vip+accounts&sp=EgIIAg%253D%253D"]




def magik(link):
	listlnk = main(link)
	for link in listlnk:
		desc_ext(link)
		print("[+] Starting Sub link")

	print("[+] upper link is in process ..data is extracting")

for link in linkss:
	magik(link)
	print("[-] Going for sleep for 5 second")
	time.sleep(5)





driver.quit()



