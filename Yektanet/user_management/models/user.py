from django.db import models
from django.contrib.auth.models import User


class User(User):
    class Meta:
        abstract = True
