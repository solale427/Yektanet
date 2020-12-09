from rest_framework import serializers
from rest_framework.serializers import Serializer


class AdViewSerializer(Serializer):
    ad = serializers.IntegerField()
    hour = serializers.DateTimeField()
    views = serializers.IntegerField(required=False)
