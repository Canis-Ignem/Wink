from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

uBlock = path_to_extension = r'C:\Users\Jon Perez\AppData\Local\Google\Chrome\User Data\Default\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.27.10_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + uBlock)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()

'''
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
driver.get("https://www.youtube.com/watch?v=SDfZY99vO3s&t=0s")
'''

#Reference to the buttons we are using
playVideo = "#ytp-id-46"
playList = "ytp-play-button ytp-button ytp-play-button-playlist"
skipVideo = "ytp-next-button ytp-button"
randomPlaylist = "Shuffle playlist"
volumeBotton = "ytp-mute-button ytp-button"

def OpenPlaylist():
    try:
        driver.get("https://www.youtube.com/watch?v=3cedABWfEBw&list=PLaLWNpJCbH_r_0jG3o4r_kUtLB1gUFUdX")
        driver.minimize_window()
        volume5()
        sleep(1)
        shuffle = driver.find_element_by_xpath('//button[@aria-label="'+randomPlaylist+'"]')
        shuffle.click()
    except:
        pass    
#Pause the current video
def pause():
    # play the video
    #wait.until(visible((By.ID, "video-title")))
    #driver.find_element_by_id("video-title").click()
    try:
        play = driver.find_element_by_xpath('//a[@href="'+playVideo+'"]')
        play.click()
    except:
        pass

#Pause the current video from a playlist
def pauseList():
    try:
        play = driver.find_element_by_xpath('//button[@class="'+playList+'"]')
        play.click()
    except:
        pass

#Skip to next video
def skip():
    try:
        skip = driver.find_element_by_xpath('//a[@class="'+skipVideo+'"]')
        skip.click()
    except:
        pass

#Sets de volume to 5%
def volume5():
    try:
        volume = driver.find_element_by_xpath('//button[@class="'+volumeBotton+'"]')
        volume.send_keys(Keys.ARROW_DOWN *19)
    except:
        pass
    





