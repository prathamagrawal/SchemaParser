from django.contrib import admin
from .models.schema import SchemaModel
from .models.properties import PropertiesModel

admin.site.register(SchemaModel)
admin.site.register(PropertiesModel)
# Register your models here.
