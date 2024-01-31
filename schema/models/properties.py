from django.db import models
from .schema import SchemaModel

class PropertiesModel(models.Model):
    schemaDetails=models.ForeignKey(SchemaModel,
                                    related_name="properties",on_delete=models.SET_NULL,
        null=True)
    
    """Repeating Fields"""
    propertyTitle=models.CharField(max_length=100)
    propertyDescription=models.CharField(max_length=200)
    propertyRequired=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.schemaDetails}"

    