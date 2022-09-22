from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from polls.models import HomeData, Park, Protect, User, News, NewsPosts, HomeIMGData


class HomeDataInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeData
        fields = "__all__"


class ProtectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protect
        fields = "__all__"


class ParkInfoSerializer(serializers.ModelSerializer):

    pos=ProtectInfoSerializer(many=True)
    class Meta:
        model = Park
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class NewsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsPostsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPosts
        fields = "__all__"


class HomeIMGDataInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeIMGData
        fields = "__all__"
