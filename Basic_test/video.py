from picamera import PiCamera

with picamera.PiCamera() as record:
	record.resolution = (1280, 480)
	record.start_recording('demo_video.h264')
	record.wait_recording(30)
	record.stop_recording()