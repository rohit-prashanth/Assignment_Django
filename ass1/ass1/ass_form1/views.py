from django.shortcuts import render
from .forms import RenderingForm
from django.http import HttpResponse

# Create your views here.
def rendering(request):
    if request.method == 'POST':
        form = RenderingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            return render(request,'rendering.html',{'form':form})

    else:
        form = RenderingForm()
        return render(request,'rendering.html',{'form':form})


def rendering1(request):
    if request.method == 'POST':
        form = RenderingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            return render(request, 'rendering1.html', {'form': form})

    else:
        form = RenderingForm()
        return render(request,'rendering1.html',{'form':form})

def rendering2(request):
    if request.method == 'POST':
        form = RenderingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            return render(request, 'rendering2.html', {'form': form})

    else:
        form = RenderingForm()
        form.order_fields(field_order=['name','text','email'])
        return render(request,'rendering2.html',{'form':form})


def rendering3(request):
    if request.method == 'POST':
        form = RenderingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            return render(request,'rendering3.html',{'form':form})

    else:
        form = RenderingForm()
        return render(request,'rendering3.html',{'form':form})