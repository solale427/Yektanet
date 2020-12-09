from django.contrib.auth.hashers import check_password
from rest_framework import views
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK
from rest_framework.authtoken.models import Token

from user_management.models import Advertiser
from user_management.serializers.advertiser import AdvertiserLoginSerializer


class AdvertiserLoginView(views.APIView):
    def post(self, request):
        serializer = AdvertiserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        advertiser = get_object_or_404(Advertiser, username=data.get('username', ''))
        password = data.get('password', '')

        if not password == advertiser.password:
            raise ValidationError(
                'پسورد اشتباه است', code=HTTP_403_FORBIDDEN
            )

        token = Token.objects.filter(user=advertiser).first()

        if not token:
            token = Token.objects.create(user=advertiser)

        return Response(
            data={
                'auth_token': token.key
            },
            status=HTTP_200_OK
        )
