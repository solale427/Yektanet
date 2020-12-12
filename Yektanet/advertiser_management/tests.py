from django.test import TestCase
from requests import Request
from rest_framework.test import APIClient, RequestsClient
from rest_framework.authtoken.models import Token

from user_management.models import nAdvertiser


