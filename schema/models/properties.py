from django.db import models
from .schema import SchemaModel

dataTypes=(
    ('int','Integer'),
    ('str','String'),
    ('bool','Boolean'),
    ('float','Decimal'),
    ('date','Date'),
)

class PropertiesModel(models.Model):
    schemaDetails=models.ForeignKey(SchemaModel,
                                    related_name="properties",on_delete=models.SET_NULL,
        null=True)
    
    """Repeating Fields"""
    propertyTitle=models.CharField(max_length=100)
    propertyDescription=models.CharField(max_length=200)
    propertyDataType=models.CharField(max_length=20,choices=dataTypes,default='str')
    propertyRequired=models.BooleanField(default=False)


    