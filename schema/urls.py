# urls.py
from django.urls import path
from .views import create_schema_model

urlpatterns = [
    path('create/', create_schema_model, name='create_schema_model')
]
