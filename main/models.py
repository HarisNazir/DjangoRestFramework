from django.db import models

# Create your models here.

class excel_generation_request(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    generated_file = models.CharField(max_length=300)