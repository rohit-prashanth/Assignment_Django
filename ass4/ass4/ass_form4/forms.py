from django import forms


class StudentFormReg(forms.Form):
    firstname = forms.CharField(initial='MR/MRS',label='Firstname',error_messages={'required':'Username should be less than 10 characters'},max_length=10)
    middlename = forms.CharField(initial='MR/MRS',label='Middlename',error_messages={'required':'Username should be less than 10 characters'},max_length=10)
    lastname = forms.CharField(initial='MR/MRS',label='Lastname',error_messages={'required':'Username should be less than 10 characters'},max_length=10)
    course = forms.CharField()
    gender = forms.CharField(label_suffix='-[M/F]')
    dob = forms.CharField(label_suffix='-[dd/mm/yyyy]')
    age = forms.IntegerField()
    project_url = forms.URLField(label_suffix="-[Enter your project url]")
    email = forms.EmailField(help_text='Enter you google email',label='Email')
    phone_num = forms.CharField(initial='+91',label='Phone number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    re_password = forms.CharField(widget=forms.PasswordInput, label='Re-Password')
    address = forms.CharField(widget=forms.Textarea,label='Address')

class EmployeeFormReg(forms.Form):
    name = forms.CharField(initial='MR/MRS',label='Username',error_messages={'required':'Username should be less than 10 characters'},max_length=10)
    gender = forms.CharField(label_suffix='-[M/F]')
    age = forms.IntegerField()
    company = forms.CharField(label='Email')
    dob = forms.CharField(label_suffix='-[dd/mm/yyyy]')
    email = forms.EmailField(help_text='Enter you google email',label='Email')
    phone_num = forms.CharField(initial='+91',label='Phone number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    re_password = forms.CharField(widget=forms.PasswordInput, label='Re-Password')

    address = forms.CharField(widget=forms.Textarea,label='Address')
