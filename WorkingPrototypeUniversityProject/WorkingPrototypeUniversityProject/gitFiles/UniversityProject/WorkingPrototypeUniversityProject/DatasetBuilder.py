#-----------------------------------this module is used to build or capture the images form the user--------------------------------------
import cv2
import os
import matplotlib.pyplot as plt
import pyData as pD


#------------------------------------Class to detect the faces-------------------------------------------------

class FaceDetector(object):
	def __init__(self, xml_path):
		self.classifier = cv2.CascadeClassifier(xml_path)

	def detect(self, image, biggest_only = True):
		sclae_factor = 1.2
		min_neighbors = 5
		min_size = (30,30)
		biggest_only = True

		flags = cv2.CASCADE_FIND_BIGGEST_OBJECT | cv2.CASCADE_DO_ROUGH_SEARCH if biggest_only else  cv2.CASCADE_SCALE_IMAGE
		facesCoord = self.classifier.detectMultiScale(image, scaleFactor = sclae_factor, minNeighbors = min_neighbors, minSize = min_size, flags = flags)
		return facesCoord




#----------------------------Detect, Cut normalize and resize face image----------------------------------------
class normalizeFaces():
	def __init__(self, frame, facesCoord):
		self.frame = frame
		self.facesCoord	= facesCoord 

		try:
			while True:
				frame = self.frame
				faces_Coord = self.facesCoord
				if len(faces_Coord):
					faces = cut_faces(frame, faces_Coord)
					faces = normalize_intensity(faces)
					faces = resize(faces)
					cv2.imshow(faces[0]) 		#or plt_show(faces[0])  to display the processed image
					clear_output(wait = True)
		except KeyboardInterrupt:
			print("the processing video in the class normalizeFaces")


#---------------------------------------TO RESIZE THE IMAGE---------------------------------------------------

def resize(images, size = (150,150)):
	image_norm = []
	for image in images:
		if image.shape<size:
			image_norm = cv2.resize(image,size,interpolation= cv2.INTER_AREA)
		else:
			image_norm = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)
	return images_norm
#--------------------------------------------Extra Functions---------------------------------------------------
def normalize_faces(frame, faces_Coord):
	faces = cut_faces(frame, faces_Coord)
	faces = normalize_intensity(faces)
	faces = resize(faces)
	return faces

def draw_rectangle(image, coords):
	for(x,y,w,h) in coords:
		w_rm = int(0.2 *w/2)
		cv2.rectangle(image,(x+w_rm,y),(x+w_rm, y+h), (150,150,0),8)

'''
#------------------------------------------Dataset Builder------------------------------------------------------
folder = 'people/'+input('Person : ').upper()				#input name											#the path for the folder will be passed as a string
cv2.namedWindow('UniversityProject-Group15', cv2.WINDOW_AUTOSIZE)

Detector = FaceDetector('Haar/haarcascade_frontalface_alt.xml')
#Detector.classifier('Haar/haarcascade_frontalface_alt.xml')

if not os.path.exists(folder):
	os.mkdir(folder)
	counter = 0
	timer = 0

	webcam = cv2.VideoCapture(0)

	while counter < 20: 										#snaps 20 pictures atleast
		frame = webcam.read()
		facesCoord = Detector.detect(image=frame) 					#to detect the faces from the person
		if len(facesCoord) and timer%700 == 50:					# this means every second or so
			faces = normalize_faces(frame,facesCoord)			#normalizing the pipeline
			cv2.imwrite(folder + '/'+ str(counter) + '.jpg', faces[0])
			plt.show(faces[0], 'ImagesSaved : ' + str(counter))
			#clear_output(wait= True)							#saved face in the notebook
			counter += 1

		draw_rectangle(frame,facesCoord) 						#draws rectangle around the face
		cv2.imshow("UniversityProject",frme)					#live feed in the external
		cv2.waitKey(50)
		timer +=50
	cv2.destroyAllWindows()
else:
	print("This name already exist")
'''