import numpy as np
import argparse
import time
import cv2
import webbrowser
import Predictor
#import Whatsapp


twitch = "https://www.twitch.tv/directory/following"
yt = "https://www.youtube.com/feed/subscriptions?flow=2"
music= "https://www.youtube.com/watch?v=3cedABWfEBw&list=PLaLWNpJCbH_r_0jG3o4r_kUtLB1gUFUdX"
bolTW = False
bolYT = False
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

print("[INFO] starting video stream...")
vs = cv2.VideoCapture(0)
time.sleep(2.0)

name = "0"

def maxPos(list):
    max = 0
    pos = 0
    for i in range(len(list)):
        if float(list[i]) > max :
            max = float(list[i])
            pos = i
    return pos

#From the names the model returns make an array with the predictions
def orderPredicciones(names):
    
	predictions = []
	predictions = str(names)
	predictions = predictions[2:len(predictions)-2]
	predictions = predictions.split(",")
	if len(predictions) < 1:
		return -1
	print("The predictions are: ")
	print(predictions)
	print()
	return predictions

#From the socres of the model get an array with the scores and the position of the highest one
def orderScores(scores):
    
	score = str(scores)[8:]
	score = score[:len(score)-2]
	points = score.split(',')
	if len(points) < 1:
		return -1,-1
	
	pos = maxPos(points)
 
	print("The scores are: ")
	print(points)
	print()
	return points, pos
    
#Main cicle
while True:

	#read from the camera
	ret, frame = vs.read()
 
	#So we dont get a null
	name = "0"


	#Get the predictions and scores fom the model
	names, scores =  Predictor.detection(frame)
	#if there are no detections do nothing
	if names != []:

		#Get predictions in an array of stings
		predictions = orderPredicciones(names)
		
		#Get the position of the maximum score and the array with the scores in str
		scores , pos = orderScores(scores)
		
		#Print the highest score prediction and save it
		if predictions != -1:
			print("Prediction: " + predictions[pos])
			name = predictions[pos]
			
		
		
		#Try and convert the highst score to a float
		try:
			Rscore= float(scores[pos])
		except ValueError:
			print("Sin detecciones")
		
		#Check prections and act accordingly, has to be above a threshhold
		if 'One' in name and Rscore > 0.6:
			
			if bolTW == False:
				counter = time.time()
				bolTW = True
				webbrowser.get(chrome_path).open(twitch)
				#Whatsapp.MensajeYara2()

			elif bolTW == True:
				counter2 = time.time()
				if counter2 - counter > 10:
					webbrowser.get(chrome_path).open(twitch)
					#Whatsapp.MensajeYara2()
					counter = time.time()
			
			
	
		elif 'Peace' in name and Rscore > 0.65:
			
			if bolYT == False:
				counter = time.time()
				bolYT = True
				webbrowser.get(chrome_path).open(yt)
				#Whatsapp.MensajeYara()

			elif bolYT == True:
				counter2 = time.time()
				if counter2 - counter > 10:
					webbrowser.get(chrome_path).open(yt)
					#Whatsapp.MensajeYara()
					counter = time.time()
		
		elif 'Fist' in name and Rscore > 0.5:
      
			if bolYT == False:
    				counter = time.time()
				bolYT = True
				webbrowser.get(chrome_path).open(music)
				#Whatsapp.MensajeYara()

			elif bolYT == True:
				counter2 = time.time()
				if counter2 - counter > 10:
					webbrowser.get(chrome_path).open(music)
					#Whatsapp.MensajeYara()
					counter = time.time()
			

		#End of analisis of a frame
		print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
	#End predictions if
 
	#Show frame on screen
	cv2.imshow("Frame", frame)
	
	#Shu down the script with the letter 'Q'
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

#Cleanup
cv2.destroyAllWindows()
