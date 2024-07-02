from django import forms

class profile_form(forms.Form):
    user_image = forms.FileField()