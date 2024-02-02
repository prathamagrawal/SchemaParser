from django.db import models

class SchemaModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"
    
    def getProperties(self):
        return ', '.join(self.properties.all().values_list('propertyTitle', flat=True))