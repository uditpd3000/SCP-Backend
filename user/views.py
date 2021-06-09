from django.http import response
from django.shortcuts import render
from django import http
from django.http.response import HttpResponse,JsonResponse
from rest_framework import viewsets,permissions,status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.serializers import Serializer
from .serializers import userserializer
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from .utils import *
from rest_framework.parsers import JSONParser

class Userview(APIView):
   def get(self,request):
       try:
           user=Isloggedin(request)
           if user is None :
               return HttpResponse("Unauthorized",status=401)
           return Response(userserializer.data,status=status.HTTP_200_OK) 
        
       except:
            return HttpResponse("Bad Request",status=400)