from django import forms
from .models import ScholoshipReg

class ScholorshipForm(forms.ModelForm):
    class Meta:
        model = ScholoshipReg
        fields = ['firstname','middlename','lastname','state','scholorship_catagory','College','aadhar_number',
                  'gender','dob','age','email','phone_num','address']

