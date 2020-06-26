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
	predictions = predictions[2:len(predictions)-1]
	predictions = predictions.split("\', ")
	print("The predictions are: ")
	print(predictions)
	print()
	return predictions

#From the socres of the model get an array with the scores and the position of the highest one
def orderScores(scores):
    
	score = str(scores)[8:]
	score = score[:len(score)-2]
	points = score.split(',')
 
	pos = maxPos(points)
 
	print("The scores are: ")
	print(points)
	print()
	print("Hihgest score is in position: " + str(pos))
	print()
	return points, pos
    
#Main cicle
while True:

	#read from the camera
	ret, frame = vs.read()
 
	#So we dont get a null
	name = "0"


	#Get the predictions and scores fom the model
	names, scores =  PyTorchTest.detection(frame)

	#Get predictions in an array of stings
	predictions = orderPredicciones(names)
	
	#Get the position of the maximum score and the array with the scores in str
	scores , pos = orderScores(scores)
	
	#Print the highest score prediction and save it
	print("Prediction: " + predictions[pos])
	name = predictions[pos]
	
	
	
	#Try and convert the highst score to a float
	try:
		Rscore= float(scores[pos])
	except ValueError:
		print("Sin detecciones")
	
	#Check prections and act accordingly, has to be above a threshhold
	if name == '\'One\'' and Rscore > 0.6:
		'''
		if bol == False:
			counter = time.time()
			bol = True
			webbrowser.get(chrome_path).open(url)

		elif bol == True:
			counter2 = time.time()
			if counter2 - counter > 10:
				webbrowser.get(chrome_path).open(url)
				counter = time.time()
		'''
		print("oneeeeeeeeeeeeeeeeeeeee")
  
	elif name == 'Peace' and Rscore > 0.6:	
		print("peaceeeeeeeeeeeeeeeeeeeee")

	#End of analisis of a frame
	print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
	#Show frame on screen
	cv2.imshow("Frame", frame)
	
	#Shu down the script with the letter 'Q'
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

#Cleanup
cv2.destroyAllWindows()
