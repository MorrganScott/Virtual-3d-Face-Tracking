#This will be an object oriented version
#of the virtual 3d game
import cv2
import numpy as np

class FaceFinder:
  #use harcaasecade filter to detect largest face from a frame
  def __init__(self):
    print('Face Finder intitialize')
    self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


  def find_face(self,frame):
    #returns face center (x,y), draws a rect on the frame
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
  #initialized with display size. draws background grid based on position
  def __init___(self):
    self.disp_h = 0
    self.disp_w = 0
    self.cam_h = 720
    self.cam_w = 1280
    self.save_x = 960

  def draw_target_xy(self, img, pos, size): #Draws the target
    cv2.circle(img, pos, size, (0, 0, 255), -1)
    cv2.circle(img, pos, int(size*.8), (255, 255, 255), -1)
    cv2.circle(img, pos, int(size*.6), (0, 0, 255), -1)
    cv2.circle(img, pos, int(size*.4), (255, 255, 255), -1)
    cv2.circle(img, pos, int(size*.2), (0, 0, 255), -1)

  def draw_targetz(self, pos, facexy):#Draws a target with its position and 
    #size relative to the user's position
    tx, ty, tz = pos
    cv2.circle(img, (targ0x, targ0y), 50, (255, 255, 0), -1)
    cv2.circle(img, (960+int((600-960)*.3**2), 540), 
     (targ0x, targ0y), (255, 255, 0), -1)
    
  def update(self, facexy): #Redraws the screen
    x,y = facexy
    e = .9
    x = e * x + (1-e*self.save_x)
    self.save_x = x
    img = np.zeros([1080,1920,3])
    decay = .3
    sx = sy = 0
    dx = int((x - self.cam_w/2)*2)
    for i in range(1,7):
      sx = sx + int((960-sx)*decay)
      sy = sy + int((540-sy)*decay)
      dx = int(dx * decay)
      #print(sx,sy)
      cv2.rectangle(img, (sx+dx,sy),(1920-sx+dx, 1080-sy), 
       (255, 255, 266), 1)#Draws targets with trainig line

      targ0x = 600 + int((x - self.cam_w/2)*2*.6)
      targ0y = 540

      cv2.line(img, (960 + int((600-960)*.3**2), 540), 
       (targ0x, targ0y), (255, 0, 0), 3)
      self.draw_target_xy(img, (targ0x, targ0y), 35)

      targ1x = 1000 + int((x - self.cam_w/2)*2*.2)
      targ1y = 440

      cv2.line(img, (960 + int((1200-960)*.3**2), 540 - int((540-340)*.3**2)), 
       (targ1x, targ1y), (255, 0, 0), 3)
      self.draw_target_xy(img, (targ1x, targ1y), 25)

      targ2x = 1000 + int((x - self.cam_w/2)*2*.9)
      targ2y = 650

      cv2.line(img, (960 + int((1100-960)*.3**2), 540 - int((540-650)*.3**2)), 
       (targ2x, targ2y), (255, 0, 0), 3)
      
      self.draw_target_xy(img, (targ2x, targ2y), 50)


    cv2.imshow("Morrgan's Game", img)#Displays the NDarray




  
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
