from detecto import utils
import argparse
import ImageResicer as IR

'''
ap = argparse.ArgumentParser()
ap.add_argument('-v', "--video", required= True, help = "path to video")
args = vars(ap.parse_args())
video = args["video"]
'''
utils.split_video('videoPeace.mp4', 'frames/' , prefix = 'Peace', step_size= 4)
size = (800, 600)
IR.rescale_images('frames/', size)

