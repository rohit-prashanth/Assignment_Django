from django import forms


class MedicalForm(forms.Form):
    name = forms.CharField(initial='MR/MRS',label='Username',error_messages={'required':'Username should be less than 10 characters'},max_length=10)
    gender = forms.CharField(label_suffix='-[M/F]')
    dob = forms.CharField(label_suffix='-[dd/mm/yyyy]')
    email = forms.EmailField(help_text='Enter you google email',label='Email')
    phone_num = forms.CharField(initial='+91',label='Phone number')
    address = forms.CharField(widget=forms.Textarea,label='Address')

