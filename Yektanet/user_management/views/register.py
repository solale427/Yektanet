from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from user_management.serializers import UserSerializer
from user_management.utils import get_auth_token


class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserSerializer
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_auth_token(user)

        return Response(
            data={
                'auth_token': token.key
            },
            status=HTTP_201_CREATED
        )
