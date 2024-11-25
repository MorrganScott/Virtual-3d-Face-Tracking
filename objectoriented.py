#This will be an object oriented version
#of the virtual 3d game
import cv2
import numpy
class FaceFinder:
  """use harcaasecade filter to detect largest face from a frame"""
  def __init__(self):
    print('Face Finder intitialize')
    self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


  def find_face(self,frame):
    """returns face center (x,y), draws a rect on the frame"""
    #convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = self.face_cascade.detectMultiScale(gray)
    #Draw rectangle
    if faces is None:
      return None
    bx=by=bw=bh=0
    for (x, y, w, h) in faces:
      if w>bw:
        bx,by,bw.bh=x,y,w,h
    cv2.rectangle(frame, (bx,by), (bx+bw, by+bh), (0, 255, 255), 5)
    return (bx+bw/2, by+bh/2)
  
#-------------------------------------------------------
#main
print('starting OO virtual3d')
ff = FaceFinder()
print('virtual3d Complete')
