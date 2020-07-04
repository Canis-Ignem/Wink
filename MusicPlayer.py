from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

uBlock = path_to_extension = r'C:\Users\Jon Perez\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.27.10_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + uBlock)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
driver.get("https://www.youtube.com/watch?v=SDfZY99vO3s&t=0s")

#Reference to the buttons we are using
playVideo = "#ytp-id-46"
playList = "ytp-play-button ytp-button ytp-play-button-playlist"
skipVideo = "ytp-next-button ytp-button"
    
#Pause the current video
def pause():
    # play the video
    #wait.until(visible((By.ID, "video-title")))
    #driver.find_element_by_id("video-title").click()
    play = driver.find_element_by_xpath('//a[@href="'+playVideo+'"]')
    play.click()

#Pause the current video from a playlist
def pauseList():
    
    play = driver.find_element_by_xpath('//button[@class="'+playList+'"]')
    play.click()

#Skip to next video
def skip():
    skip = driver.find_element_by_xpath('//a[@class="'+skipVideo+'"]')
    skip.click()
    
    

wait = WebDriverWait(driver, 3)

sleep(2)

skip()




