from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
from keras.models import load_model
from time import sleep
from keras.preprocessing import image





face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
classifier =load_model('./Emotion_Detection.h5')
class_labels = ['Angry','Happy','Neutral','Sad','Surprise']


class VideoCamera(object):
	def __init__(self):
		self.cap = cv2.VideoCapture(0)
	
	def __del__(self):
		self.cap.release()

	def get_frame(self):
		# success, image = self.video.read()
		# # We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# # so we must encode it into JPEG in order to correctly display the
		# # video stream.

		# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		# for (x, y, w, h) in faces_detected:
		# 	cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		# frame_flip = cv2.flip(image,1)
		# ret, jpeg = cv2.imencode('.jpg', frame_flip)
		# return jpeg.tobytes()
		ret, frame = self.cap.read()
		labels = []
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces = face_classifier.detectMultiScale(gray,1.3,5)
		
		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h,x:x+w]
			roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)


			if np.sum([roi_gray])!=0:
				roi = roi_gray.astype('float')/255.0
				roi = img_to_array(roi)
				roi = np.expand_dims(roi,axis=0)

			# make a prediction on the ROI, then lookup the class

				preds = classifier.predict(roi)[0]
				print("\nprediction = ",preds)
				label=class_labels[preds.argmax()]
				print("\nprediction max = ",preds.argmax())
				print("\nlabel = ",label)
				label_position = (x,y)
				cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
			else:
				cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
			print("\n\n")
			#cv2.imshow('Emotion Detector',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		ret, jpeg = cv2.imencode('.jpg', frame)
		return jpeg.tobytes()
		
			






