from django.shortcuts import render, redirect
from .forms import SchemaModelForm,PropertiesFormset
from django.http import HttpResponse
from .models.properties import PropertiesModel
from .models.schema import SchemaModel

def create_schema_model(request):
    if request.method == 'GET':
        schemaform = SchemaModelForm(request.GET or None)
        formset = PropertiesFormset(queryset=PropertiesModel.objects.none())

    elif request.method == 'POST':
        formset = PropertiesFormset(request.POST)
        schemaform = SchemaModelForm(request.POST)
        if schemaform.is_valid() and formset.is_valid():
            book = schemaform.save()
            for form in formset:
                property = form.save(commit=False)
                property.schemaDetails = book
                property.save()
            return HttpResponse("Success")
        

    return render(request, 'create_schema.html', {
        'schemaform': schemaform,
        'formset': formset,
    })
