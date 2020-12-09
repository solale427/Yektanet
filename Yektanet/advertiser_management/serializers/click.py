from rest_framework import serializers
from rest_framework.serializers import Serializer


class ClickSerializer(Serializer):
    ad = serializers.IntegerField()
    hour = serializers.DateTimeField()
    clicks = serializers.IntegerField(required=False)
