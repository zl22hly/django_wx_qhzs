from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from polls.models import Park, Posts,Protect,NewsPosts,News,HomeData


class HomeDataInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeData
        fields = "__all__"


class ParkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = "__all__"


class ProtectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protect
        fields = "__all__"