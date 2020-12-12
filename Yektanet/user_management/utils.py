from rest_framework.authtoken.models import Token


def get_auth_token(user):
    token = Token.objects.filter(user=user).first()

    if not token:
        token = Token.objects.create(user=user)

    return token