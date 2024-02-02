from django.shortcuts import render
from ..forms.add import SchemaModelForm,PropertiesFormset
from ..models.properties import PropertiesModel


def create_schema_model(request):
    if request.method == 'GET':
        schemaform = SchemaModelForm(request.GET or None)
        formset = PropertiesFormset(queryset=PropertiesModel.objects.none())

    elif request.method == 'POST':
        formset = PropertiesFormset(request.POST)
        schemaform = SchemaModelForm(request.POST)
        if schemaform.is_valid() and formset.is_valid():
            formset_instance=formset.save(commit=False)
            schemaData = schemaform.save()
            for form in formset_instance:
                form.schemaDetails = schemaData
                form.save()

            data = schemaform.cleaned_data
            property=formset.cleaned_data
            data['properties'] = {property_item['propertyTitle']: property_item for property_item in property}
            print(data)
            return render(request, 'success.html',{'schemaData':schemaData,'propertyData':formset_instance,'jsonResponse':data})

    return render(request, 'create_schema.html', {
        'schemaform': schemaform,
        'formset': formset,
    })

