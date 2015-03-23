""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((40,40),'uint8')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    for (x,y,w,h) in faces:
        frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)

        cv2.rectangle(frame,(x+w/5,y+7*w/20),(x+2*w/5,y+9*w/20),(255,255,255),-1)
        cv2.rectangle(frame,(x+w/5,y+7*w/20),(x+2*w/5,y+9*w/20),(0,0,0),1)
        cv2.rectangle(frame,(x+11*w/40,y+15*w/40),(x+13*w/40,y+17*w/40),(0,0,255),-1)

        cv2.rectangle(frame,(x+3*w/5,y+7*w/20),(x+4*w/5,y+9*w/20),(255,255,255),-1)
        cv2.rectangle(frame,(x+3*w/5,y+7*w/20),(x+4*w/5,y+9*w/20),(0,0,0),1)
        cv2.rectangle(frame,(x+27*w/40,y+15*w/40),(x+29*w/40,y+17*w/40),(255,0,0),-1)

        cv2.circle(frame, (x+5*w/10, y+16*w/20),w/5,(0,0,0),-1)
        cv2.circle(frame, (x+5*w/10, y+16*w/20),w/6,(0,0,255),-1)
        
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()