from picamera import PiCamera
#https://picamera.readthedocs.io/en/release-1.13/recipes1.html
class CameraControl:
    def __init(self, cameraName):
        self.name = name

    def startCamera(self):
        self.camera = PiCamera()
        camera.resolution = (1920,1080)
        sleep(2)
    def stopCamera (self):
        print('stop')