from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time



class Signin :
	def __init__(self, username, pwd) :		#Constructor
		self.username = username
		self.pwd = pwd

	def click_sign_in (self):	#Selecting SIGN IN button in home page of youtube
		self.driver = webdriver.Chrome(ChromeDriverManager(version="88.0.4324.96").install())
		self.driver.get("https://youtube.com")
		time.sleep(2)
		self.driver.find_element_by_xpath("//ytd-button-renderer[@class='style-scope ytd-masthead style-suggestive size-small']").click()
	
	def sign_in(self) :			#Google sign-in
		self.driver.find_element_by_xpath("//input[@type='email']").send_keys(self.username)
		self.driver.find_element_by_xpath("//input[@type='email']").send_keys(Keys.RETURN)
		time.sleep(2)
		self.driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
		self.driver.find_element_by_xpath("//input[@type='password']").send_keys(Keys.RETURN)
		time.sleep(2)

	def search(self) :			#Code to select video section
		# self.channel = input("Enter Channel name")
		self.channel = "DISGUISED TOAST"
		self.driver.find_element_by_xpath("//input[@id='search']").send_keys(self.channel)
		self.driver.find_element_by_xpath("//input[@id='search']").send_keys(Keys.RETURN)
		time.sleep(2)
		self.name_channel = self.driver.find_element_by_xpath("//*[@id='content-section']")
		self.name_channel.click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//*[@id='tabsContent']/paper-tab[2]").click()

	def scroll(self) :			#Scrolling through all the videos
		scroll_pause = 2
		last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
		while True:
			self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
			time.sleep(scroll_pause)
			new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
			if new_height == last_height:
				print("\nScrolling Finished!\n")
				break
			last_height = new_height
			print("\nScrolling")

	def videos(self) :
		all_videos = self.driver.find_elements_by_xpath("//*/ytd-grid-renderer/div/ytd-grid-video-renderer/div/ytd-thumbnail/a['@id=thumbnail']")
		links = [elm.get_attribute('href') for elm in all_videos]
		bot = self.driver
		for x in links :
			bot.get(x)
			time.sleep(2)
			like = bot.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]")
			like_btn = bot.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]/a")
			if like.get_attribute("class") == "style-scope ytd-menu-renderer force-icon-button style-default-active" :
				print("Already Liked the video")
				time.sleep(1)
				continue
			else :
				like_btn.click()
				print("Liked the video now")
				time.sleep(1)


def initiate ():
	username = input("Enter your Email/Phone number : ")
	password = input("Enter password : ")
	obj = Signin(username, password)
	obj.click_sign_in()
	obj.sign_in()
	obj.search()
	obj.scroll()
	obj.videos()
	print("Thanks for testing :)\n")

initiate()
