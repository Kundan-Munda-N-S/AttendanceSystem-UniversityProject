'''
images = 'list of numpy arrays'
labels = numpyt array with the labels corresponding to the images
'''

def collect_dataset():
	images = []
	labels = []
	labels_dict = {}
	people = [person for person in os.listdir('people/')]																									#create a list of the person's names or ID's
	for i,person in enumerate(people):
		labels, dic[i] = person
		for images in os.listdir('people/'+person):
			images.append(cv2.imread('people/'+person+'/'+image,0)) #0/o refer page 4 or timestamp 57:07
			labels.append(i)
	return (images,np.array(labels), labels_dict)																											



#---------------------------COLLECT THE IMAGE DATA AND TRAIN THE MODEL----------------------------------

images, labels, labels_dict = collect_dataset()
rec_eig = cv2.face.EigenFaceRecognizer_create()
rec_eig.train(images, labels)

#neets atleast two people 

rec_fisher = cv2.face.FisherFaceRecognizer_create()
rec_fisher.train(images, labels)

rec_lbph = cv2.face.LBPHFaceRecognizer_create()
rec_lbph.train(images, labels)

print('*'*20+'models trained successfully'+'*'*20)

