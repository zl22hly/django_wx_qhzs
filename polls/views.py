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
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .serializers import ParkInfoSerializer, HomeDataInfoSerializer, ProtectInfoSerializer, UserInfoSerializer, \
    NewsInfoSerializer, NewsPostsInfoSerializer, HomeIMGDataInfoSerializer
from .models import HomeData, Park, Protect, User, News, NewsPosts, HomeIMGData
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django import forms

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer


class HomeView(ModelViewSet):
    queryset = HomeData.objects.all()
    serializer_class = HomeDataInfoSerializer


class NewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsInfoSerializer


class NewsPostsView(ModelViewSet):
    queryset = NewsPosts.objects.all()
    serializer_class = NewsPostsInfoSerializer


class HomeIMGDataView(ModelViewSet):
    queryset = HomeIMGData.objects.all()
    serializer_class = HomeIMGDataInfoSerializer


class ParkView(ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = ParkInfoSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)  # 指定过滤器
    search_fields = ('fullname', 'id')  # 指定可搜索的字段
    filterset_fields = ('fullname', 'id')


class ProtectView(ModelViewSet):
    queryset = Protect.objects.all()
    serializer_class = ProtectInfoSerializer
    # filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)  # 指定过滤器
    # search_fields = ('name2', )  # 指定可搜索的字段
    # filterset_fields = ('name2', )


class parkFormAdd(forms.ModelForm):
    class Meta:
        model = Park
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}


def home_list(request):
    queryset = User.objects.all()
    return render(request, 'home.html')


def park_list(request):
    queryset = Park.objects.all()
    return render(request, 'park.html', {'queryset': queryset})


def park_add(request):
    if request.method == "GET":
        form = parkFormAdd()
        return render(request, 'parkadd.html', {'form': form})
    form = parkFormAdd(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/parklist/")
    else:
        return render(request, 'parkadd.html', {'form': form})


def park_delete(request):
    nid = request.GET.get("nid")
    Park.objects.filter(id=nid).delete()
    return redirect("/parklist/")


def park_edit(request, nid):
    row_object = Park.objects.filter(id=nid).first()
    return render(request, 'parkedit.html', {"row_object": row_object})