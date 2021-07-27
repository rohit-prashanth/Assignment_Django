from django.shortcuts import render
from .forms import MedicalForm

# Create your views here.
def medical(request):
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            return render(request, 'rendering.html', {'form': form})

    else:
        form = MedicalForm()
        return render(request, 'rendering.html', {'form': form})