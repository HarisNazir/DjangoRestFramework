from django.shortcuts import render

from .forms import GetCountry

# Create your views here.
def index(request):
    form = GetCountry()
    return render(request, 'country_form.html', {'form': form})