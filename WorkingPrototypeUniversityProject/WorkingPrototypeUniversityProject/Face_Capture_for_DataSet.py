# -------------------- THIS IS USED TO CAPTURE STORE THE PHOTOS TO TRAIN THE FACE RECOGNITION SYSTEMS ------------------
#-----------------------------------------UNIVERSITY_PROJECT_GROUP-15---------------------------------------------------

'''
	REQUIREMENTS:
		HaarFiles = {face and eyes}
		videoCameraSource = for caturing the photos for storing in the dataset

		I/P :	frames from the video_Source
				name/id-no
		O/P :	tilt filtered cropped faces stored in the dataSet folder

'''

import sys
import cv2                  # Importing the opencv
import numpy as np          # Import Numarical Python
import NameFind
import os
WHITE = [255, 255, 255]		#WHITE COLOR RATIO
RED = [255 , 0 , 0]				#RED COLOR RATIO FOR RGB-FORMAT
GREEN = [132 , 222 , 2]			#GREEN COLOR RATIO FOR RGB-FORMAT

#   import the Haar cascades for face ditection

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

ID = NameFind.AddName()
Count = 0
cap = cv2.VideoCapture(0)                                                                           # Camera object

os.mkdir('dataSet/'+ID)
path =  'dataset/'+ID

#path = 'dataSet/'            #os.getcwd()
while Count < 50:
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(np.average(gray))                                                    # Converts the video Frames to graySe
    if np.average(gray) > 85:#110:                                                                   # Testing the brightness of the image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
        print(faces)                                      											 # Detect the faces and store the positions
        for (x, y, w, h) in faces:  

            NameFind.draw_box(gray, x, y, w, h)
            FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]    # The Face is isolated and cropped
            Img = (NameFind.DetectEyes(FaceImage))
            cv2.putText(gray, "FACE DETECTED", (x+(w//2), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
            if Img is not None:
                frame = Img                                                                         # Show the detected faces
            else:
                frame = gray[y: y+h, x: x+w]
            
            cv2.imwrite(path+"/" +str(ID)+'.'+str(Count) + ".jpg", frame)
            cv2.waitKey(300)
            cv2.imshow("CAPTURED PHOTO", frame)                                                     # show the captured image
            print("Count\t:",Count)
            Count = Count + 1
            
    cv2.imshow('DETECTING FACES FOR THE DATASET', gray)                                       		# To Show the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print ('FACE CAPTURE IS COMPLETED SUCCESSFULLY!')
cap.release()
cv2.destroyAllWindows()
