from main.models import excel_generation_request
import pytest

@pytest.mark.django_db
@pytest.mark.celery(result='redis://')
def test_StatusDone(client, celery_worker):
    client.post('api/generate-excel?country=FRA')

    assert excel_generation_request.objects.count() == 1
    obj = excel_generation_request.objects.all()[0]
    assert obj.status != 'pending'