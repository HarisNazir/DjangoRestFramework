from main.models import excel_generation_request
from .celery import app
import requests
from main.generatefile import GenerateExcelFile

@app.task     
def generate_excel(excel_generation_request_id):
    data = excel_generation_request.objects.get(id = excel_generation_request_id)
    res = requests.get(f"https://restcountries.eu/rest/v2/alpha/{data.country}")
    join_data = res.json()
    GenerateExcelFile(join_data, data)
    data.status = "done"
    data.save()