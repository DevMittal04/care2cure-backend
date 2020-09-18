from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
import json

from .models import User, Anonymous_User, Counsellor, Article
from .serializers import UserSerializer, LoginSerializer, AnonymousSerializer, CounsellorSerializer, ArticleSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

# Create your views here.
'''
def createUser(info):
      profilePic = info["profilePic"]
      email = info["email"]
      name = info["name"]
      dob = info["dob"]
      contact = info["contact"]
      address = info["address"]

class UserCRUD(APIView):

    def get(self, request, format="json"):
        info = json.loads((request.body).decode('utf-8'))
        create = createUser(info)
        return JsonResponse(create,safe=False)
'''

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

# Sign Up API
@api_view(['POST'])
def CreateUser(request):
    serializer = UserSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_503_SERVICE_UNAVAILABLE)

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