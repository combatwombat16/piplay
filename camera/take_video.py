import sys
sys.path.append("../")
from picamera import PiCamera
from time import sleep
from initialize import init_video

with PiCamera() as camera:
	init_video(camera)
	camera.start_preview()
	sleep(1)
	camera.start_recording('./videos/test.h264')
	sleep(10)
	camera.stop_preview()
