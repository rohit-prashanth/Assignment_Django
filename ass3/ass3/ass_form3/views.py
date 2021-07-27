from django.shortcuts import render

# Create your views here.
from .forms import SocialForm

# Create your views here.
def social(request):
    if request.method == 'POST':
        form = SocialForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            return render(request, 'rendering.html', {'form': form})

    else:
        form = SocialForm()
        return render(request, 'rendering.html', {'form': form})