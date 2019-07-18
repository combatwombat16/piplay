import sys
sys.path.append("../")
from picamera import PiCamera
from time import sleep
from initialize import init_picture

with PiCamera() as camera:
	init_picture(camera)
	camera.start_preview()
	sleep(1)
	camera.capture('./pictures/test_initialized.jpg')
	
	for i in camera.IMAGE_EFFECTS:
		sleep(.25)
		camera.image_effect = i
		camera.capture('./pictures/test_ie_%s.jpg' % i)
		sleep(.25)
	init_picture(camera)

	for i in camera.AWB_MODES:
		sleep(.25)
		camera.awb_mode = i
		camera.capture('./pictures/test_awb_%s.jpg' % i)
		sleep(.25)
	init_picture(camera)

	for i in camera.EXPOSURE_MODES:
		sleep(.25)
		camera.exposure_mode = i
		camera.capture('./pictures/test_em_%s.jpg' % i)
		sleep(.25)
	init_picture(camera)
	
	camera.stop_preview()
