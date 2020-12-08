from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertiser_management.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'link', 'image']

    def create(self, validated_data):
        if not validated_data['link'].startswith('http'):
            raise ValidationError('Link should start with http')

        return super().create(validated_data)
