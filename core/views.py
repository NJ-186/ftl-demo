from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import USER, ActivityPeriod
from .serializers import USERSerializer, ActivityPeriodSerializer

# Create your views here.

@api_view(['GET'])
def home(request):
    users = USER.objects.all()
    user_serializer = USERSerializer(users, many = True)

    res = {
        "ok" : True,
        "members" : user_serializer.data
    }

    return Response(res , status = status.HTTP_200_OK)