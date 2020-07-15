import numpy as np
import argparse
import time
import cv2
import webbrowser
import Predictor
import numpy
#import Whatsapp
import MusicPlayer



music= "https://www.youtube.com/watch?v=Nj2U6rhnucI&list=PLyORnIW1xT6waC0PNjAMj33FdK2ngL_ik"
bolTW = False
bolYT = False
bolMusic = False
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

print("[INFO] starting video stream...")
vs = cv2.VideoCapture(0)
#time.sleep(2.0)

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
def getPredictions(names):
    
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
def getScores(scores):
    
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

def getBox(boxes):
    
	boxesAux = []
	for box in boxes:
		boxesAux.append(box)
		break

	try:
     
		box = str(boxesAux)[9:]
		box = box[:len(box)-3]
		aux = box.split(",")
		boxes = []

		for i in range(len(aux)):
			a= float(aux[i])
			boxes.append(int(a))
		
		return boxes
	except ValueError:
			return -1;
    
    
#Main cicle
while True:

	#read from the camera
	ret, frame = vs.read()
 
	#So we dont get a null
	name = "0"


	#Get the predictions and scores fom the model
	names, scores, boxes =  Predictor.detection(frame)
	box = getBox(boxes)


	#if there are no detections do nothing
	if names != []:

		#Get predictions in an array of stings
		predictions = getPredictions(names)
		
		#Get the position of the maximum score and the array with the scores in str
		scores , pos = getScores(scores)
		
		#Print the highest score prediction and save it
		if predictions != -1:
			print("Prediction: " + predictions[pos])
			name = predictions[pos]
			
		
		
		#Try and convert the highst score to a float
		try:
			Rscore= float(scores[pos])
		except ValueError:
			print("No detections")
		
		#Check prections and act accordingly, has to be above a threshhold
		if 'Palm' in name and Rscore > 0.9:
			
			if bolTW == False:
				counter = time.time()
				bolTW = True
				MusicPlayer.pauseList()

			elif bolTW == True:
				counter2 = time.time()
				if counter2 - counter > 2:
					MusicPlayer.pauseList()
					counter = time.time()
			
			
	
		elif 'Peace' in name and Rscore > 0.9:
			
			if bolYT == False:
				counter = time.time()
				bolYT = True
				MusicPlayer.skip()

			elif bolYT == True:
				counter2 = time.time()
				if counter2 - counter > 2:
					MusicPlayer.skip()
					counter = time.time()
		
		elif 'Ok' in name and Rscore > 0.9:
      
			if bolMusic == False:
				counter = time.time()
				bolMusic = True
				MusicPlayer.OpenPlaylist()

			elif bolMusic == True:
				counter2 = time.time()
				if counter2 - counter > 2:
					MusicPlayer.OpenPlaylist()
					counter = time.time()
			

		#End of the frame analisis
		print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
	#End predictions if
 
	#Cuadrado
	#if box != -1 and Rscore > 0.7:
	#	cv2.rectangle(frame, (box[0],box[1]), (box[2],box[3]), (255,0,0),2 )
	# un comment to show frame on screen 
	#cv2.imshow("FrameQ", frame)
	
	#Shu down the script with the letter 'Q'
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		MusicPlayer.close()
		break

#Cleanup
cv2.destroyAllWindows()
