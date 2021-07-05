from django.shortcuts import render
from .forms import GetCountry
import requests

# Create your views here.
def index(request):
    form = GetCountry(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            iso_code = form.cleaned_data['iso3']
            return AddToModel(iso_code)
    return render(request, 'country_form.html', {'form': form})

def AddToModel(iso_code):
    res = requests.get(f"https://restcountries.eu/rest/v2/alpha/{iso_code}")
