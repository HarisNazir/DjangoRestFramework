from django.shortcuts import render
from .forms import GetCountry
import requests
from .models import excel_generation_request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from celery import Celery
from .generatefile import GenerateExcelFile

app = Celery('hello', broker='amqp://guest@localhost//')
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

class ExcelGenerationRequest(APIView):
    def get(self, request, format="None"):
        database_id = request.query_params["id"]
        status = self.GetCountryStatus(database_id)
        return Response(status)

    def GetCountryStatus(self, database_id):
        obj = excel_generation_request.objects.get(id=database_id)
        return obj.status

@app.task     
def generate_excel(excel_generation_request_id):
    data = excel_generation_request.objects.get(id = excel_generation_request_id)
    res = requests.get(f"https://restcountrcountryies.eu/rest/v2/alpha/{data.country}")
    join_data = res.json()
    GenerateExcelFile(join_data)
    data.status = "done"
    data.save()

