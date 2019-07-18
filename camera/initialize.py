#! /usr/bin/python3

def init_picture(camera):
        camera.resolution = (2592, 1944)
        camera.framerate = 15
        camera.awb_mode = 'auto'
        camera.image_effect = 'none'
        camera.exposure_mode = 'auto'

def init_video(camera):
        camera.resolution = (1920, 1080)
        camera.framerate = 30
        camera.awb_mode = 'auto'
        camera.image_effect = 'none'
        camera.exposure_mode = 'auto'
