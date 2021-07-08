from django.urls import path

from . import views

urlpatterns = [
    path('', views.HelloWorld.as_view()),
    path('api/generate-excel', views.GenerateExcel.as_view(), name='get-country'),
    path('api/check-status', views.ExcelGenerationRequest.as_view(), name='check-status'),
    path('api/excel-generation-request/<int:id>/download', views.Download.as_view(), name="Download")
]