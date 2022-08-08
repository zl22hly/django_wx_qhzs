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
urlpatterns = [
    url(r'homelist/', views.home_list),
    url(r'parklist/', views.park_list),
    url(r'parkadd/', views.park_add),
    url(r'parkdelete/', views.park_delete),
    url(r'parkedit/<int:nid>/', views.park_edit),
]
router = DefaultRouter()
# router.register(r'^register/$', views.registerView.as_view(), basename="register")

router.register(r'home', views.HomeView, basename="homeData")

# router2 = DefaultRouter()
router.register(r'pack', views.ParkView, basename="ParkData")

# router3 = DefaultRouter()
router.register(r'Protect', views.ProtectView, basename="ProtectData")

router.register(r'user', views.UserView, basename="UserData")

router.register(r'news', views.NewsView, basename="NewsData")

router.register(r'newsPosts', views.NewsPostsView, basename="NewsPostsData")

router.register(r'HomeIMGData', views.HomeIMGDataView, basename="HomeIMGDataData")

# urlpatterns = [
#     path(r'', include(router.urls)),
#
#     path(r'', include(router2.urls)),
# ]

urlpatterns += router.urls

