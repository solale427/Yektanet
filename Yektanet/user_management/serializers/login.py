from rest_framework import serializers
from rest_framework.serializers import Serializer


class LoginSerializer(Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
