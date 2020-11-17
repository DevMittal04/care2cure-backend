from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
import json
from django.utils import timezone
import datetime
import re

from .models import User, Anonymous_User, Counsellor, Article, AgeMorbidityChart, StateDisorderChart, SuicidalRiskChart, HumanResourcesChart, Profile, ChatBots, MentalStates
from .serializers import UserSerializer, LoginSerializer, AnonymousSerializer, CounsellorSerializer, ArticleSerializer, AgeMorbidityChartSerializer, StateDisorderChartSerializer, SuicidalRiskChartSerializer, HumanResourcesChartSerializer, ProfileSerializer, ChatBotSerializer, MentalStatesSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from authentication.careChat import ProcessChat

from django.http.response import StreamingHttpResponse
from authentication.camera import VideoCamera

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

# Single User Details API
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

# MentalStates API
@api_view(['GET'])
def ShowMentalStates(request,pk):
    state = MentalStates.objects.filter(email=pk)
    serializer = MentalStatesSerializer(state, many=True)
    return Response(serializer.data)

# Anonymous User APIs
# List of all the anonymous users API (for testing purpose)
@api_view(['GET'])
def UserAnonymousDetail(request):
    user_detail = Anonymous_User.objects.all()
    serializer = AnonymousSerializer(user_detail, many=True)
    return Response(serializer.data)

# Single Anonymous User Details API
@api_view(['GET'])
def ParticularAnonymousUserDetail(request,pk):
    anonyUser = Anonymous_User.objects.get(id=pk)
    serializer = AnonymousSerializer(anonyUser, many=False)
    return Response(serializer.data)

# Create Anonymous User API
# @api_view(['POST'])
# def CreateUserAnonymous(request):
#     serializer = AnonymousSerializer(data=request.data)
#     if(serializer.is_valid()):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 #Delete Anonymous User Account API
@api_view(['DELETE'])
def DeleteUserAnonymous(request,pk):
    user = Anonymous_User.objects.get(id=pk)
    user.delete()
    print("User deleted")
    return Response("Your Data is Deleted")

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

# Charts APIs
# Age Morbidity Chart API
@api_view(['GET'])
def DisplayAgeMorbidityChart(request):
    rows = AgeMorbidityChart.objects.all()
    serializer = AgeMorbidityChartSerializer(rows,many=True)
    return Response(serializer.data)

# State Disorder Chart API
@api_view(['GET'])
def DisplayStateDisorderChart(request):
    rows = StateDisorderChart.objects.all()
    serializer = StateDisorderChartSerializer(rows,many=True)
    return Response(serializer.data)

# Sucidial Risk Chart API
@api_view(['GET'])
def DisplaySuicidalRiskChart(request):
    rows = SuicidalRiskChart.objects.all()
    serializer = SuicidalRiskChartSerializer(rows,many=True)
    return Response(serializer.data)

# Human Resources Chart API
@api_view(['GET'])
def DisplayHumanResourcesChart(request):
    rows = HumanResourcesChart.objects.all()
    serializer = HumanResourcesChartSerializer(rows,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def MentalHealthChart(request,pk):
    rows = MentalStates.objects.filter(email=pk)
    serializer = MentalStatesSerializer(rows, many=True)
    return Response(serializer.data)

# ChatBot Kommunicate
@api_view(['POST'])
def Chat(request):
    ques_list = ["okay","sejal gupta created group Conversations","We are here for you . do not worry ! We are here to ask you a few questions just to understand how you feel!", "We are here to help you! We are here to ask you a few questions just to understand how you feel!", "Do you ever feel nervous within yourself and angry because of it?", "Do you end up in a situation where you are out of control and suddenly feel intense fear?", "Do you feel tensed sometimes and does that lead to heavy breathing?", "Do you often feel sweaty?", "Do you often feel lost even while you are in a group?", "Do you sleep more/less than 6-10 hours?", "Do you often feel negative about everything around you and that you cannot do it?", "Do you feel like unable to give proper efforts and concentration to your work , be it college, school or office?", "Do you lose control over control over small things?", "Do you feel like your reactions are sometimes way too much for a given situation?", "Have you felt that you have started eating less/more than you used to?", "Were there circumstances where you have thought of giving up?", "Do you feel tired  without doing anything?", "Do you have people you can trust/rely on?", "Are you active  on Social Media?", "Do you feel like your weight has increased/decreased?", "Do you often find yourself surrounded with material things more compared to people?", "Do you feel shy interacting with people?", "Do you often think of stressful bad memories from past?", "Do you often cancel on plans", "Do you often feel things will not work the way you want it to?", "Do you feel like things that are happening with you are the consequences of your actions", "Do you dream something bad often?", "Did not get you? We are here to make  you understand how you feel! To answer the question send 'okay' and reply in yes or no mostly :) Thank You!", "Thank You For Answering! You did amazing! Proud! Wait for a while and you will get your report."]
    serializer = ChatBotSerializer(data=request.data)
    if(serializer.is_valid()):
        if(serializer.validated_data['message'] not in ques_list):
            print("Valid data")
            print(serializer.validated_data['message'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif(serializer.validated_data['message'] == "Thank You For Answering! You did amazing! Proud! Wait for a while and you will get your report."):
            group_id = serializer.validated_data['groupId']
            print(group_id)
            # Retriving groupId of the user who completed the chat and then mapping it with users meta email
            group = ChatBots.objects.filter(groupId=group_id).order_by('key')
            user = group.first()
            uid = user.metadata['KM_CHAT_CONTEXT']
            uid = uid[10:]
            uid1 = uid[:-2]
            print(uid1)
            b = []
            for a in group:
                if(a.message=='yes'):
                    b.append(1)
                elif(a.message=='no'):
                    b.append(0)
            result = ProcessChat(b)
            user = User.objects.get(email=uid1)
            row = MentalStates.objects.create(email=user,state=result)
            return Response("Done")
        else:
            return Response("Invalid Data")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Emotion Capture APIs

def gen(camera):
	while True:
		#yield(camera.get_frame())
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')

# Test APIs

@api_view(['GET'])
def testChat(request):
    c = [1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1]
    result = ProcessChat(c)
    user = User.objects.get(email="gsejal222@gmail.com")
    row = MentalStates.objects.create(email=user,state=result)
    return Response("Done")

# @api_view(['GET'])
# def testSenti(request):
#     c = ["Yes", "No"]
#     for line in c:
#         analysis = TextBlob(line) 
#     # set sentiment 
#         if analysis.sentiment.polarity > 0: 
#             print('positive')
#         elif analysis.sentiment.polarity == 0: 
#             print('neutral')
#         else: 
#             print('negative')

#     return HttpResponse("Done")

@api_view(['GET'])
def testAnony(request):
    user = Anonymous_User.objects.get(id=3)
    print(str(user.id)+"_"+user.username)
    return Response("Done")

@api_view(['POST'])
def testMakeAnony(request):
    CUser = Anonymous_User.objects.create()
    # SUser = Anonymous_User.objects.get(id=CUser.id)
    # print(SUser)
    d = {id : CUser}
    serializer = AnonymousSerializer(data=d, many=False)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)