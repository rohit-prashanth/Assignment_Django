from django.shortcuts import render
from .forms import ScholorshipForm
from .models import ScholoshipReg

# Create your views here.
def scholor(request):
    if request.method == 'POST':
        form = ScholorshipForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            middlename = form.cleaned_data['middlename']
            state = form.cleaned_data['state']
            scholorship_catagory = form.cleaned_data['scholorship_catagory']
            College = form.cleaned_data['College']
            aadhar_number = form.cleaned_data['aadhar_number']
            gender = form.cleaned_data['gender']
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            phone_num = form.cleaned_data['phone_num']
            address = form.cleaned_data['address']
            stu = ScholoshipReg(firstname=firstname,middlename=middlename,lastname=lastname,state=state,gender=gender,dob=dob,phone_num=phone_num,address=address,age=age,email=email)
            stu.save()
            return render(request, 'Thankyou.html')

    else:
        form = ScholorshipForm()
        return render(request, 'renderingscholor.html', {'form': form})

