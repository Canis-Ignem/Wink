from detecto import utils
import argparse

'''
ap = argparse.ArgumentParser()
ap.add_argument('-v', "--video", required= True, help = "path to video")
args = vars(ap.parse_args())
video = args["video"]
'''
utils.split_video('video.mp4', 'frames/' ,step_size= 4)


