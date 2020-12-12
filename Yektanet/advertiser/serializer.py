from rest_framework import serializers
from rest_framework.authtoken.admin import User

from advertiser.models import Advertiser


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'
