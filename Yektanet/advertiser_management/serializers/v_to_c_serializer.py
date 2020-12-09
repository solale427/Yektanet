from rest_framework import serializers
from rest_framework.serializers import Serializer


class ViewToClickSerializer(Serializer):
    ad_id = serializers.IntegerField()
    hour = serializers.DateTimeField()
    ratio = serializers.FloatField(required=False)