# import os
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls .")
# def test(request):
#     return HttpResponse("Hello.")
# -------------------------
# from rest_framework import serializers
# from polls.models import park
# from rest_framework import serializers
# ++++++++++

from rest_framework.viewsets import ModelViewSet
from .serializers import ParkInfoSerializer, HomeDataInfoSerializer,ProtectInfoSerializer
from .models import HomeData, Park,Protect


class HomeView(ModelViewSet):
    queryset = HomeData.objects.all()
    serializer_class = HomeDataInfoSerializer


class ParkView(ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = ParkInfoSerializer


class ProtectView(ModelViewSet):
    queryset = Protect.objects.all()
    serializer_class = ProtectInfoSerializer