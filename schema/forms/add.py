from django import forms
from django.forms import modelformset_factory

from ..models.schema import SchemaModel
from ..models.properties import PropertiesModel


class SchemaModelForm(forms.ModelForm):
    class Meta:
        model = SchemaModel
        fields = ('title', 'description', )
        labels = {
            'title': 'Schema Title:',
            'description': 'Schema Description:'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Schema title here'
                }
            ),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Schema description here'
                }
            )
        }


PropertiesFormset = modelformset_factory(
    PropertiesModel,
    fields=('propertyTitle','propertyDescription','propertyDataType','propertyRequired',),
    extra=1,
    widgets={
        'propertyTitle': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Property title here'
        }),
        'propertyDescription': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Property Description here'
        }),
        'propertyDataType': forms.Select(attrs={
            'class': 'form-control',
        }),
        'propertyRequired': forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'placeholder': 'Select if the field is required: '
        }),
    }
)
