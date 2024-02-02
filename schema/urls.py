# urls.py
from django.urls import path
from .views.home import home
from .views.create import create_schema_model
from .views.upload import upload


urlpatterns = [
    path('',home,name="home"),
    path('create/', create_schema_model, name='create_schema_model'),
    path('upload/',upload,name='upload')
]
