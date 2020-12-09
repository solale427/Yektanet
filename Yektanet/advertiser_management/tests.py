from django.test import TestCase
from requests import Request
from rest_framework.test import APIClient, RequestsClient
from rest_framework.authtoken.models import Token

from user_management.models import Advertiser
import requests

data = {
    'title': 'hi',
    'link': '',
    'image': '',
    'advertiser_username': 'ali'
}

url = 'http://127.0.0.1:8000/advertiser_management/ad/'
headers = {'Authorization': 'Token 14107cafeaaf07e379e9f7af956604a39d694f5f'}
r = requests.post(url=url,data=data, headers=headers)
print(r)

