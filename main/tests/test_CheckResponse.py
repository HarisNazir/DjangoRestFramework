from main.views import GenerateExcel
import pytest
from main.models import excel_generation_request

# ResultURL = GenerateExcel.data

# def CheckResultURLTest(ResultURL):
#     assert ResultURL == "/api/excel-generation-request/1", "Incorrect URL"

@pytest.mark.django_db
def test_CheckResponseTest(client):
    obj = excel_generation_request(
        country = "FRA",
        status = "pending",
        generated_file = "test.xlsx"
    )
    obj.save()

    response = client.get(f"/api/check-status?id={obj.id}")
    assert response.status_code == 200
    assert response.json() == "pending"
