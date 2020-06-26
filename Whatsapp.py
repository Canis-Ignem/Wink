from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from io import StringIO
from io import BytesIO
import win32clipboard
from PIL import Image

driver = webdriver.Chrome('U:\Documents\Proyectos\Wink\chromedriver.exe') 
driver.get('http://web.whatsapp.com')


def copyImageToClipboard(path):
   
   filepath = path
   image = Image.open(filepath)  
    
   output = BytesIO()
   image.convert("RGB").save(output, "BMP")
   data = output.getvalue()[14:]
   output.close()
       
   win32clipboard.OpenClipboard()
   win32clipboard.EmptyClipboard()
   win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
   win32clipboard.CloseClipboard()





def mensajeCualquiera():
       
   k = input('Pulsa M para enviar un mensaje F para enviar una foto: ')
   if k == 'm' or k == 'M':
      
      name = input('A quien quieres mandar el mensaje?: ')
      user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
      user.click()
      
      msg = input('Enter the message : ')
      msg = " " + msg
      
      msg_box = driver.find_element_by_class_name('_3uMse')
      msg_box.send_keys(msg+ Keys.ENTER)
      
   if k == 'f' or k == 'F':
          
      name = input('A quien quieres mandar el mensaje?: ')
      user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
      user.click()
      
      msg = input('Enter the message : ')
      msg = " " + msg
      
      path = input('donde esta tu foto : ' )
      copyImageToClipboard(path)
      
      
      msg_box = driver.find_element_by_class_name('_3uMse')
      msg_box.send_keys(msg + Keys.CONTROL + "v")
      sleep(0.3)
      send = driver.find_element_by_class_name('_6TTaR')
      send.click()
   
        
def MensajeYara():
   
      name = 'Yara'
      user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
      user.click()
      
      msg = "ILY"
      
      msg_box = driver.find_element_by_class_name('_3uMse')
      msg_box.send_keys(msg+ Keys.ENTER)
