from detecto import core, utils, visualize
import cv2
dataset = core.Dataset('frames/')
#model = core.Model(['Wink','NWink'])
model = core.Model.load('Gestures2.pth',['One','Peace'])
#model = core.Model()

#visualize.detect_live(model)

#image = utils.read_image('prueba.png')

def detection(image):

  labels, boxes, scores = model.predict_top(image)
  return labels, scores
