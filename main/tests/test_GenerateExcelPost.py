from main.views import GenerateExcel
import pytest
from main.models import excel_generation_request
from rest_framework.response import Response

# ResultURL = GenerateExcel.data

# def CheckResultURLTest(ResultURL):
#     assert ResultURL == "/api/excel-generation-request/1", "Incorrect URL"

@pytest.mark.django_db
def test_GenerateExcel(client):
    client.post('/api/generate-excel?country="FRA"')

    assert excel_generation_request.objects.count() == 1
    obj = excel_generation_request.objects.all()[0]
    assert obj.country == "FRA"

    assert Response("/api/excel-generation-request/1") == f"/api/excel-generation-request/{obj.id}"