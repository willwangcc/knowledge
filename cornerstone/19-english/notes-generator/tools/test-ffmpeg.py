# from subprocess import call
# call('ls')
# call('ffmpeg -ss 00:00:05 -i sintel.mp4 -vframes 1 -q:v 2 output.jpg')
import os 
os.system('ffmpeg -ss 00:00:05 -i sintel.mp4 -vframes 1 -q:v 2 output.jpg')
