from django.http import response
from main.views import GenerateExcel
import pytest
from main.models import excel_generation_request
from rest_framework.response import Response

@pytest.mark.django_db
def test_GenerateExcel(client):
    response = client.post('/api/generate-excel?country=FRA')

    assert excel_generation_request.objects.count() == 1
    obj = excel_generation_request.objects.all()[0]
    assert obj.country == "FRA"
    assert response.json()["result-url"] == f"/api/generate-excel/{obj.id}"