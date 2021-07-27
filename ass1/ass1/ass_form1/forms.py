from django import forms
from django.core import validators

class RenderingForm(forms.Form):
    name = forms.CharField(initial='MR/MRS',label='Username',validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField(help_text='Enter you google email',label='Email')
    text = forms.CharField(widget=forms.Textarea,label='Text Field')

