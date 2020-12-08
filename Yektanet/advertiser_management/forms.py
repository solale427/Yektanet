from django import forms
from django.core.exceptions import ValidationError


class AdForm(forms.Form):
    link = forms.CharField(label='link', max_length=200, required=True)
    image = forms.CharField(label='image', max_length=200, required=True)
    title = forms.CharField(label='title', max_length=50, required=True)
    advertiser_username = forms.CharField(label='advertiser_username',max_length=50, required=True)

    def clean_link(self):
        if not self.data['link'].startswith('http'):
            raise ValidationError('Link should start with http')

        return self.data['link']
