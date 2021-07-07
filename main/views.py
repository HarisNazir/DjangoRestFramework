from django.shortcuts import render
from .forms import GetCountry
import requests
from .models import excel_generation_request
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorld(APIView):

    def get(self, request, format="None"):
        return Response("Hello World!")

    def post(self, request, format="None"):
        data  = {"result_url": "/api/excel-generation-request/1"}
        return Response(data)
    
class GenerateExcel(APIView):
    
    def post(self, request, format="None"):
        country = request.query_params["country"]
        AddToModel(country)
        return Response(country)

    def AddToModel(country):
        res = requests.get(f"https://restcountries.eu/rest/v2/alpha/{country}")
        data = res.join()
        excel_generation_request.object.create(
            country = data.get('name'),
            status = 'pending',
        )
        

# Create your views here.
# def index(request):
#     form = GetCountry(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             iso_code = form.cleaned_data['iso3']
#             return AddToModel(iso_code)
#     return render(request, 'country_form.html', {'form': form})



