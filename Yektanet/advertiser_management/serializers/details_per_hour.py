from rest_framework import serializers
from rest_framework.serializers import Serializer


class DetailsPerHourSerializer(Serializer):
    ad_id = serializers.IntegerField()
    ratio = serializers.FloatField(required=False)
    views = serializers.IntegerField(required=False)
    hour = serializers.DateTimeField()
    clicks = serializers.IntegerField(required=False)
