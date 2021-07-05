from django.db import models

# Create your models here.

class excel_generation_request(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField()
    status = models.CharField()
    generated_file = models.CharField()