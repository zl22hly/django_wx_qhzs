# from django.contrib import admin
# from django.contrib.messages import api
# from django.urls import path, include
# from . import views
#
# urlpatterns = [
#     path('login/', views.NewsInfo),
# ]
from django.urls import path, include
from django.conf.urls import url

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'home', views.HomeView, basename="homeData")

router2 = DefaultRouter()
router2.register(r'pack', views.ParkView, basename="ParkData")

router3 = DefaultRouter()
router3.register(r'Protect', views.ProtectView, basename="ProtectData")

urlpatterns = []
urlpatterns += router.urls
urlpatterns += router2.urls
urlpatterns += router3.urls
