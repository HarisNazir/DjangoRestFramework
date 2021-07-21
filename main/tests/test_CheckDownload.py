from main.models import excel_generation_request
import pytest
import time

@pytest.mark.celery(result='redis://')
@pytest.mark.django_db(transaction=True)
def test_CheckDownload(client, celery_worker):
    response = client.post('/api/generate-excel?country=FRA')
    assert response.status_code == 200

    time.sleep(5)
    
    assert excel_generation_request.objects.count() == 1
    obj = excel_generation_request.objects.all()[0]
    assert obj.status != 'pending'

    response = client.get(f'/api/excel-generation-request/{obj.id}/download')
    # breakpoint()
    assert response['Content-Disposition'] == f'inline; filename="{obj.generated_file}"'
