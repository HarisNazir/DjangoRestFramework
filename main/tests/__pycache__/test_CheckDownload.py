from main.models import excel_generation_request
import pytest

def test_CheckDownload(client):
    client.post('api/generate-excel?country=FRA')

    assert excel_generation_request.objects.count() == 1
    obj = excel_generation_request.objects.all()[0]
    assert obj.status != 'pending'

    response = client.post(f'api/excel-generation-request/{obj.id}/download')
    assert response['Content-Disposition'] == f'attachment; {obj.name}-{obj.id}.xlsx'