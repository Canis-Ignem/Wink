import numpy as np
import argparse
import time
import cv2
import webbrowser
import PyTorchTest


url = "https://www.twitch.tv/directory/following"
bol = False
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
COLORS = np.random.uniform(0, 255, size=(2, 3))

print("[INFO] starting video stream...")
vs = cv2.VideoCapture(0)
time.sleep(2.0)
bol = False



while True:

	ret, frame = vs.read()
	idx = 0
	
	names, scores =  PyTorchTest.detection(frame)
	print(names)
	name = str(names)[1:6]
	print(name)
	score = str(scores)[8:14]
	print(score)
	try:
		Rscore= float(score)
	except ValueError:
		print("Sin detecciones")
     
	if name == '\'One\'' and Rscore > 0.6:
		if bol == False:
			counter = time.time()
			bol = True
			webbrowser.get(chrome_path).open(url)

		elif bol == True:
			counter2 = time.time()
			if counter2 - counter > 10:
				webbrowser.get(chrome_path).open(url)
				counter = time.time()
				
		
		
  
   
      

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break


cv2.destroyAllWindows()
