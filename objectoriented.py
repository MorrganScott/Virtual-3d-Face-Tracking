#This will be an object oriented version
#of the virtual 3d game
import cv2

class Tunnel: 

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
        bx,by,bw,bh=x,y,w,h
    cv2.rectangle(frame, (bx,by), (bx+bw, by+bh), (0, 255, 255), 5)
    return (bx+bw/2, by+bh/2)

class Satge():
  """initialized with display size. draws background grid based on position."""
  def __init___(self):
    self.disp_h = 0
    self.disp_w = 0
    self.cam_h = 720
    self.cam_w = 1280
    self.save_x = 960

  def draw_target_xy(self, img, pos, size): #draws the target
    cv2.circle(img, pos, size, (0, 0, 255), -1)
    cv2.circle(img, pos, int(size*.8), (255, 255, 255), -1)
    cv2.circle(img, pos, int(size*.6), (0, 0, 255), -1)
    cv2.circle(img, pos, int(size*.4), (255, 255, 255), -1)
    cv2.circle(img, pos, int(size*.2), (0, 0, 255), -1)

  
#-------------------------------------------------------
#main
print('starting OO virtual3d')
ff = FaceFinder()
#create cam/ FaceFinder Instance
cap = cv2.VideoCapture(cv2.CAP_ANY)
if not cap.isOpened():
  print("Couldn't open cam")
  exit()




while True:
  #pass
  retval, frame = cap.read()
  if retval == False:
    print("camera error!")

  ff.find_face(frame)
  cv2.imshow('q to quit', frame)
  
  if cv2.waitKey(30) == ord('q'):
    break





pause = input('press enter to end')

#destroy cam
cap.release()

cv2.destroyAllWindows()
print('virtual3d Complete')
