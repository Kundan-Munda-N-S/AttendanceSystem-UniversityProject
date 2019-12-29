#-----------------------------------------importing required modules-------------------------------
import numpy as np
import os
import math
from matplotlib import pyplot as plt 
#matplotlib inline
import cv2
#print(cv2.__version__)




#----------------------------------------DEFINING IMPORTANT METHODS--------------------------------

def plt_show(image, title = ''):
	if len(image, shape) == 3:
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		plt.axis('off')
		plt.title(title)
		plt.imshow(image, cmap = 'Greys_r')
		plt.show


#-------------------------------------------let's take a picture------------------------------------

webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()																			#ret = BooleanValue		frame = image/videoFrame
print(ret)
webcam.release()																					#to release the webcam


#---------------------------------------How about showing the read image?---------------------------
#----------RESIZABLE WINDOW-------------
cv2.startWindowThread()																				#open's a new thread to manage the external cv2 interaction
#cv2.namedWindow('UniversityProject-Group15', cv2.WINDOW_NORMAL)										#create a window holder to show the read image
#cv2.imshow("UniversityProject-Group15", frame)


#-------------------------------------FIX THE WINDOW------------------------------------------------

cv2.namedWindow('UniversityProject-Group15',cv2.WINDOW_AUTOSIZE)									#creating a window holder to show the read image
cv2.imshow('UniversityProject-Group15',frame)





#--------------------------------------WRITE/SAVE AN IMAGE--------------------------------------

cv2.imwrite('image/picture_GBR.jpg',frame)


#cv2.imwrite('image/picture_RGB.jpg',frae_RGB)

cv2.waitKey()																						#Press any key to close the external window
cv2.destroyAllWindows()

