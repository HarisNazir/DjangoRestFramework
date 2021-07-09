from drf.tasks import generate_excel
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')

from django.shortcuts import render
import requests
from .models import excel_generation_request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from celery import Celery
from .generatefile import GenerateExcelFile
from django.http import FileResponse
from django.http.response import FileResponse


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
        breakpoint()
        generate_excel.apply_async([id])
        return Response(data)

    def AddToModel(self, country):

        instance = excel_generation_request(
            country = country,
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



class Download(APIView):
    def get(self, request, id, format="None"):
        database_id = self.kwargs['id']
        obj = excel_generation_request.objects.get(id=database_id)
        if obj.status == "pending":
            return Response(obj.status)
        else:
            response = FileResponse(open(obj.generated_file, 'rb'))
            return response
