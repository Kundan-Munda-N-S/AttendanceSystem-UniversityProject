import DatasetBuilder as DB 
import trainingModel.startTraining  as trained 
import pyData as pD 
import cv2 
import os

xmlHaarPath = 'Haar/haarcascade_frontalface_alt.xml'

#--------------------------------------------------------CLASS definition( Video_Camera )----------------------------------------------

class VideoCamera(object):
	def __init__(self, index =0 ):
		self.video = cv2.VideoCapture(index)																							#index defines the camera number. Here, bydefault 0 = webcamera		
			self.index = index
		print(self.video.isOpened())

	def __del__(self):
		self.video.read()

	def get_frame(self, in_grayScale = False):
		_, frame = self.video.read()																									#to release to video by itself
		if in_grayScale:
			frame = cv2.cvtColor(frame, cv2.COLOR.BGR2GRAY)																				#converts the frame/image to grayScale
		return frame


#--------------------------------------------------------TO PASS AN SOURCE IMAGE-------------------------------------------------------

webcam = VideoCamera()
frame = webcam.get_frame()																												#returns a grayScale image

detector = DB.FaceDetector('xmlHaarPath')
frame = webcame.get_frame()

faces_Coord = detector.detect(frame)
faces = DB.normalize_faces(frame,faces_Coord)
face = faces[0]
cv2.imshow(face)

del webcam

#------------------------------------------GIVING PREDICTIONS USING THE THREE MODELS-----------------------------------------------------
	#--------------predictions using EigenFace algorithm---------------------
collector = cv2.face.StandardCollector_create()		
trained.rec_eig.predict(face, collector)																												#this line should terminate or release the webcam object
confidence = collector.getMinDist()
prediction = collector.getMinLabel()

print("Eigen Faces ---> Prediction : "+ labels_dict[prediction].capitalize() + '\tConfidence : '+ str(round(confidence))

	#--------------predictions using FisherFace algorithm---------------------

trained.rec_fisher.predict(face, collector)																												#this line should terminate or release the webcam object
confidence = collector.getMinDist()
prediction = collector.getMinLabel()

print("Fisher Faces ---> Prediction : "+ labels_dict[prediction].capitalize() + '\tConfidence : '+ str(round(confidence))

	#--------------predictions using LBPH algorithm---------------------

trained.rec_lbph.predict(face, collector)																												#this line should terminate or release the webcam object
confidence = collector.getMinDist()
prediction = collector.getMinLabel()

print("LBPH Faces ---> Prediction : "+ labels_dict[prediction].capitalize() + '\tConfidence : '+ str(round(confidence))

#---------------------------------------ANOTHER DATASET TRAINING MODELS-------------------------------------


#---------------------------LOAD IMAGES, LOAD LABELS AND TRAIN MODEL----------------------------------------
images, labels, labels_dict = collect_dataset()
rec_eig = cv2.face.EigenFaceRecognizer_create()
rec_eig.train(images, labels)

#neets atleast two people 

rec_fisher = cv2.face.FisherFaceRecognizer_create()
rec_fisher.train(images, labels)

rec_lbph = cv2.face.LBPHFaceRecognizer_create()
rec_lbph.train(images, labels)

print('*'*20+'models trained successfully'+'*'*20)


#==========================================FACE DETECTION MODEL===============================================

detector = DB.FaceDetector('xmlHaarPath')
webcam = VideoCamera(0)

cv2.namedWindow("UniversityProject - Group 15 ", cv2.WINDOW_AUTOSIZE)

while True:
	frame = webcam.get_frame()
	faces_Coord = detector.detect(frame,True)	 																#detects more than one fce

	if len(faces_Coord):
		faces = normalize_faces(frame, faces_Coord) 															#normal pipeline

		for i,face in enumerate(faces):
			collector = cv2.face.StandardCollector_create()
			rec_lbph.predict(face,collector)
			confidence = collector.getMinDist()
			prediction = collector.getMinLabel()
			threshold = 140 																					#need to determine the threshold by trial and error method or by ploting the graphs and observing them

			print('Prediction : '+labels_dict[prediction].capitalize()+'\n\tConfidence : '+str(round(confidence)))
			cv2.putText(frame, labels_dict[prediction].capitalize(),(faces_Coord[i][0], faces_Coord[i][1]-10),cv2.FONT_HERSHEY_PLAIN, 3, (66,53,243),2)
		clear_output(wait=True)

		draw_rectangle(frame, faces_Coord) #rectangle around the face
	cv2.putText(frame, "ESC to exit", (5,frame.shape[0]-5), cv2.FONT_HERSHEY_PLAIN, 1.3, (66,53,243),2,cv2.LINE_AA)
	cv2.imshow("UniversityProject - GROUP15", frame)															#live feed in external window

	if cv2.waitKey(40) & 0xFf == 27:
		cv2.destroyAllWindows()
		break


#---------------------------------Recognizing the faces using the Threshold Value-------------------------------

cv2.namedWindow("UniversityProject - GROUP15", cv2.WINDOW_AUTOSIZE)


while True:
	frame = webcam.get_frame()
	faces_Coord = detector.detect(frame,True)	 																#detects more than one fce

	if len(faces_Coord):
		faces = normalize_faces(frame, faces_Coord) 															#normal pipeline

		for i,face in enumerate(faces):
			collector = cv2.face.StandardCollector_create()
			rec_lbph.predict(face,collector)
			confidence = collector.getMinDist()
			prediction = collector.getMinLabel()
			threshold = 140 																						#need to determine the threshold by trial and error method or by ploting the graphs and observing them

			print('Prediction : '+labels_dict[prediction].capitalize()+'\n\tConfidence : '+str(round(confidence)))
			clear_output(wait=True)


		#{------------the code part where the threshold value is applied to recognize the faces ------------------
		if confidence < threshold:
			cv2.putText(frame, labels_dict[prediction].capitalize(),(faces_Coord[i][0], faces_Coord[i][1]-10),cv2.FONT_HERSHEY_PLAIN, 3, (66,53,243),2)
		else:
			cv2.putText(frame, "UNKNOWN FACE",(faces_Coord[i][0], faces_Coord[i][1]-10),cv2.FONT_HERSHEY_PLAIN, 3, (66,53,243),2)

		#---------------end of the threshold applied code ---------------------------------------------------------}
		draw_rectangle(frame, faces_Coord) #rectangle around the face
	cv2.putText(frame, "ESC to exit", (5,frame.shape[0]-5), cv2.FONT_HERSHEY_PLAIN, 1.3, (66,53,243),2,cv2.LINE_AA)
	cv2.imshow("UniversityProject - GROUP15", frame)															#live feed in external window

	if cv2.waitKey(40) & 0xFf == 27:
		cv2.destroyAllWindows()
		break


#del webcam
#webcam = VideoCamera(1)						#to change the webcamera for multiple screen live recognition

#---------------------------defining a method/behaviour/function for drawing labels using the threshold value--------

def draw_label(image, text, coord, conf, thresh):
	if conf<threshold:			#applying the threshold
		cv2.putText(image, labels_dict[prediction].capitalize(),(faces_Coord[i][0], faces_Coord[i][1]-10),cv2.FONT_HERSHEY_PLAIN, 3, (66,53,243),2)

	else:
		cv2.putText(frame,"UNKNOWN FACE",(faces_Coord[i][0], faces_Coord[i][1]-10),cv2.FONT_HERSHEY_PLAIN, 3, (66,53,243),2)

		#------------------------CODE SEGMENT FOR LIVE RECOGNITION FROM DOUBLE FRAME/CAMERAS----------------------------

		def live_recognition(index, webcam):
			global double_frame
			detector = DB.FaceDetector('xmlHaarPath')

			while True:
				frame = webcam.get_frame()
				faces_Coord = detector.detect(frame,True)	 																#detects more than one fce

				if len(faces_Coord):
					faces = normalize_faces(frame, faces_Coord) 															#normal pipeline

					for i,face in enumerate(faces):
					collector = cv2.face.StandardCollector_create()
					rec_lbph.predict(face,collector)
					confidence = collector.getMinDist()
					prediction = collector.getMinLabel()
					threshold = 140 																						#need to determine the threshold by trial and error method or by ploting the graphs and observing them

					draw_label(frame, labels_dict[prediction],(faces_Coord[i][0], faces_Coord[i][1]-10),confidence,threshold)
					draw_rectangle(frame, faces_Coord) #rectangle around the face
				
				cv2.putText(frame, "ESC to exit", (5,frame.shape[0]-5), cv2.FONT_HERSHEY_PLAIN, 1.3, (66,53,243),2,cv2.LINE_AA)
	
				if index == 0:
					cv2.putText(frame, "LAPTOP WEBCAM", (5,frame.shape[0]-5), cv2.FONT_HERSHEY_PLAIN, 1.3, (66,53,243),2,cv2.LINE_AA)

				else:
					cv2.putText(frame, "EXTERNAL CAMERA", (5,frame.shape[0]-5), cv2.FONT_HERSHEY_PLAIN, 1.3, (66,53,243),2,cv2.LINE_AA)


				double_frame[0:481, index*640:(index+1)*640] = frame 																#copies a new frame i.e. enables to display two frames as a single frame
				cv2.imshow("UniversityProject - GROUP15",double_frame)																#live feed in external window

				if cv2.waitKey(40) & 0xFf == 27:
					cv2.destroyAllWindows()
					break
