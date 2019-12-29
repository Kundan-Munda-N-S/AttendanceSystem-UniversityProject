# -------------------------- FACE DITECTION USING HAAR CASCADES ---------------------------
# ---------------------------- UNIVERSITY_PROJECT-GROUP-15---- ----------------------------
'''
#requirements:
	haarFiles = {face and eye}
	cameraInput = here, VideoCapture(0)

	I/P = StreamOfImages || video frames from the camera 
	O/P = live Video marking the detected faces

'''

import cv2                  # Importing the opencv
import NameFind				# userDefined Module for easy functioning of the operations

# import the Haar cascades for face and eye detection

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    # Convert the Camera IMAGE to gray
    # ---------------------------------- FACE DETECTION ------------------------------------

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)             # Detect the faces and store the positions
    for (x, y, w, h) in faces:                                      # Frames  LOCATION X, Y  WIDTH, HEIGHT
        gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))  # The Face is isolated and cropped	
        eyes = eye_cascade.detectMultiScale(gray_face)
        for (ex, ey, ew, eh) in eyes:
           #print(ex,' = ex', ey,'  = ey',ew,'  = ew',eh,'  = eh')	#to eliminate to recognize the tilted faces
           NameFind.draw_box(gray, x, y, w, h)						#to Draw the boxes in the gray_converted image

    cv2.imshow('Face Detection Using Haar-Cascades ', gray)         # Show the video
    if cv2.waitKey(1) & 0xFF == ord('q'):                           # Quit if the key is Q
        break

cv2.destroyAllWindows()
