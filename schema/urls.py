# urls.py
from django.urls import path
from .views.home import home
from .views.create import create
from .views.upload import upload
from .views.update import modify,selectSchema

urlpatterns = [
    path('',home,name="home"),
    path('create/', create, name='create'),
    path('upload/',upload,name='upload'),
    path('update/',selectSchema,name='selectSchema'),
    path('modify/',modify,name="update"),
]
