from rest_framework import views
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK
from user_management.models.user import User
from user_management.serializers.advertiser import AdvertiserLoginSerializer
from user_management.utils import get_auth_token


class LoginView(views.APIView):
    def post(self, request):
        serializer = AdvertiserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = get_object_or_404(User, username=data.get('username'))
        password = data.get('password')

        if not user.check_password(password):
            raise ValidationError(
                'پسورد اشتباه است', code=HTTP_403_FORBIDDEN
            )

        token = get_auth_token(user)

        return Response(
            data={
                'auth_token': token.key
            },
            status=HTTP_200_OK
        )
