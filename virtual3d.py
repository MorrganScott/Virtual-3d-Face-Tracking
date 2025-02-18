import cv2
import numpy as np
import matplotlib.pyplot

print('Launching virtual3d.')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
#img = cv2.imread('monalisa.jpg')

# Convert into grayscale
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(gray)



cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    #detectMultScale returns an 2d ndarray
    faces = face_cascade.detectMultiScale(gray)
    print('detected face(s) at:', faces)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 5)
      cv2.rectangle(frame, (x-5, y-5), (x+w+5, y+h+5), (0, 0, 0), 5)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




print('virtual3d complete')
