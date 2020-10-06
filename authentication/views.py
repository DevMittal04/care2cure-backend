from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
import json

from .models import User, Anonymous_User, Counsellor, Article, AgeMorbidityChart, StateDisorderChart, SuicidalRiskChart, HumanResourcesChart, Profile
from .serializers import UserSerializer, LoginSerializer, AnonymousSerializer, CounsellorSerializer, ArticleSerializer, AgeMorbidityChartSerializer, StateDisorderChartSerializer, SuicidalRiskChartSerializer, HumanResourcesChartSerializer, ProfileSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser



'''
PyPower Projects
Emotion Detection Using AI
'''

#USAGE : python test.py

from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np





# Registered Users APIs

# List of all the users API (for testing purpose)
@api_view(['GET'])
def UserDetail(request):
    user_detail = User.objects.all()
    serializer = UserSerializer(user_detail, many=True)
    return Response(serializer.data)

# Login API
@api_view(['GET'])
def UserLogin(request,pk):
    user_detail = User.objects.get(email=pk)
    serializer = LoginSerializer(user_detail, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ParticularUserDetail(request,pk):
    user_detail = User.objects.get(email=pk)
    serializer = UserSerializer(user_detail, many=False)
    return Response(serializer.data)


# Sign Up API
@api_view(['POST'])
def CreateUser(request):
    serializer = UserSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Registered User Details API
@api_view(['PUT'])
def UpdateUser(request,pk):
    user = User.objects.get(email=pk)
    serializer = UserSerializer(instance=user,data=request.data,partial=True)  # partial true enables us to update the row partially
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Registered User Account API
@api_view(['DELETE'])
def DeleteUser(request,pk):
    user = User.objects.get(email=pk)
    user.delete()
    print("User deleted")
    return Response("Your Data is Deleted")


# Anonymous User APIs

# List of all the anonymous users API (for testing purpose)
@api_view(['GET'])
def UserAnonymousDetail(request):
    user_detail = Anonymous_User.objects.all()
    serializer = AnonymousSerializer(user_detail, many=True)
    return Response(serializer.data)

# Create Anonymous User API
@api_view(['POST'])
def CreateUserAnonymous(request):
    serializer = AnonymousSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Update Registered User Details API
@api_view(['PUT'])
def UpdateUserAnonymous(request,pk):
    user = Anonymous_User.objects.get(username=pk)
    serializer = AnonymousSerializer(instance=user,data=request.data,partial=True)  # partial true enables us to update the row partially
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Counsellors APIs

# List of all the counsellors API (for testing purpose)
@api_view(['GET'])
def CounsellorDetail(request):
    counsellor = Counsellor.objects.all()
    serializer = CounsellorSerializer(counsellor, many=True)
    return Response(serializer.data)

# Add Counsellor Profile API
@api_view(['POST'])
def AddCounsellor(request):
    serializer = CounsellorSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Counsellor Profile API
@api_view(['PUT'])
def UpdateCounsellor(request,pk):
    counsellor = Counsellor.objects.get(id=pk)
    serializer = CounsellorSerializer(instance=counsellor,data=request.data,partial=True)  # partial true enables us to update the row partially
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Counsellor Profile API
@api_view(['DELETE'])
def DeleteCounsellor(request,pk):
    counsellor = Counsellor.objects.get(id=pk)
    counsellor.delete()
    return Response("Counsellor Profile has been Deleted")


#Articles APIs

# Add Article API
@api_view(['POST'])
def AddArticle(request):
    serializer = ArticleSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List Article API
@api_view(['GET'])
def ListArticle(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article, many=True)
    return Response(serializer.data)

# Update Article API
@api_view(['PUT'])
def UpdateArticle(request,pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article,data=request.data,partial=True)  # partial true enables us to update the row partially
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Article API
@api_view(['DELETE'])
def DeleteArticle(request,pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return Response("Counsellor Profile has been Deleted")



#Age Morbidity Chart API
@api_view(['GET'])
def DisplayAgeMorbidityChart(request):
    rows = AgeMorbidityChart.objects.all()
    serializer = AgeMorbidityChartSerializer(rows,many=True)
    return Response(serializer.data)

#State Disorder Chart API
@api_view(['GET'])
def DisplayStateDisorderChart(request):
    rows = StateDisorderChart.objects.all()
    serializer = StateDisorderChartSerializer(rows,many=True)
    return Response(serializer.data)

#Sucidial Risk Chart API
@api_view(['GET'])
def DisplaySuicidalRiskChart(request):
    rows = SuicidalRiskChart.objects.all()
    serializer = SuicidalRiskChartSerializer(rows,many=True)
    return Response(serializer.data)

#Human Resources Chart API
@api_view(['GET'])
def DisplayHumanResourcesChart(request):
    rows = HumanResourcesChart.objects.all()
    serializer = HumanResourcesChartSerializer(rows,many=True)
    return Response(serializer.data)

#Emotion Capture
@api_view(['GET'])
def EmotionCapture(request):

    face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    classifier =load_model('./Emotion_Detection.h5')

    class_labels = ['Angry','Happy','Neutral','Sad','Surprise']

    cap = cv2.VideoCapture(0)



    while True:
        # Grab a single frame of video
        ret, frame = cap.read()
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
                cv2.imshow('Emotion Detector',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()


#Dialog Flow
@api_view(['POST'])
def AddProfile(request):
    serializer = ProfileSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)