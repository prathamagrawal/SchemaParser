# urls.py
from django.urls import path
from .views.home import home
from .views.create import create
from .views.upload import upload
from .views.update import update


urlpatterns = [
    path('',home,name="home"),
    path('create/', create, name='create'),
    path('upload/',upload,name='upload'),
    path('update/',update,name='update')
]
