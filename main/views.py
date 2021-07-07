from django.shortcuts import render
from .forms import GetCountry
import requests
from .models import excel_generation_request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class HelloWorld(APIView):

    def get(self, request, format="None"):
        return Response("Hello World!")

    def post(self, request, format="None"):
        data  = {"result_url": "/api/excel-generation-request/1"}
        return Response(data)
    
class GenerateExcel(APIView):
    
    def post(self, request, format="None"):
        country = request.query_params["country"]
        id = self.AddToModel(country)
        url = f"/api/generate-excel/{id}"
        data = {"result-url": url,}

        return Response(data)

    def AddToModel(self, country):
        res = requests.get(f"https://restcountries.eu/rest/v2/alpha/{country}")
        data = res.json()

        instance = excel_generation_request(
            country = data.get('name'),
            status = 'pending',
        )
        instance.save()
        
        return instance.id

        

# Create your views here.
# def index(request):
#     form = GetCountry(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             iso_code = form.cleaned_data['iso3']
#             return AddToModel(iso_code)
#     return render(request, 'country_form.html', {'form': form})



