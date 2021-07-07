from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('helloworld/', views.HelloWorld.as_view()),
    path('api/generate-excel', views.GenerateExcel.as_view(), name='get-country')
]