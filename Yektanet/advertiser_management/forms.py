from django import forms

from .models import Ad

class AdForm(forms.Form):
    link = forms.CharField(label='link', max_length=200)
    image = forms.CharField(label='image', max_length=200)
    title = forms.CharField(label='title', max_length=50)
    advertiser_id = forms.IntegerField(label='advertiser_id')