from main.models import excel_generation_request
import pytest
import time


@pytest.mark.celery(result='redis://')
@pytest.mark.django_db(transaction=True)
def test_StatusDone(client, celery_worker):
    client.post('/api/generate-excel?country=FRA')
    time.sleep(5)
    assert excel_generation_request.objects.count() == 1
    obj = excel_generation_request.objects.all()[0]
    assert obj.status != 'pending'