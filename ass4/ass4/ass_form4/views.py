from django.shortcuts import render
from .forms import EmployeeFormReg,StudentFormReg
from .models import EmployeeReg, StudentReg


# Create your views here.
def student(request):
    if request.method == 'POST':
        form = StudentFormReg(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            middlename = form.cleaned_data['middlename']
            course = form.cleaned_data['course']
            gender = form.cleaned_data['gender']
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            project_url = form.cleaned_data['project_url']
            email = form.cleaned_data['email']
            phone_num = form.cleaned_data['phone_num']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            address = form.cleaned_data['address']
            stu = StudentReg(firstname=firstname,middlename=middlename,lastname=lastname,course=course,gender=gender,dob=dob,project_url=project_url,phone_num=phone_num,password=password,address=address,age=age,email=email,re_password=re_password)
            stu.save()
            return render(request, 'Thankyou.html')

    else:
        form = StudentFormReg()
        return render(request, 'renderingstu.html', {'form': form})

def employee(request):
    if request.method == 'POST':
        form = EmployeeFormReg(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            gender = form.cleaned_data['gender']
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            phone_num = form.cleaned_data['phone_num']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            address = form.cleaned_data['address']
            stu = EmployeeReg(name=name, company=company,
                              gender=gender, dob=dob, phone_num=phone_num, password=password,
                              address=address, age=age, email=email, re_password=re_password)
            stu.save()
            return render(request, 'Thankyou.html')

    else:
        form = EmployeeFormReg()
        return render(request, 'renderingemp.html', {'form': form})