from django.shortcuts import render
from ..forms.add import SchemaModelForm, PropertiesFormset
from ..models.properties import PropertiesModel
from ..functions.redisConnection import instantiateRedis, destroyRedis
import json


# Using redis to store schema details for faster access, (testing with 10 seconds)
def create(request):
    if request.method == "GET":
        schemaform = SchemaModelForm(request.GET or None)
        formset = PropertiesFormset(queryset=PropertiesModel.objects.none())

    elif request.method == "POST":
        formset = PropertiesFormset(request.POST)
        schemaform = SchemaModelForm(request.POST)
        if schemaform.is_valid() and formset.is_valid():
            formset_instance = formset.save(commit=False)
            schemaData = schemaform.save()
            for form in formset_instance:
                form.schemaDetails = schemaData
                form.save()

            data = schemaform.cleaned_data
            propertyFormResponse = formset.cleaned_data
            properties = [
                {key: value for key, value in item.items() if key not in ["id"]}
                for item in propertyFormResponse
            ]
            data["properties"] = properties
            try:
                cache = instantiateRedis()
                val = json.dumps(data)
                cache.set(f"schema_{data['title']}", val)
                cache.expire("schema", 180)
                destroyRedis(cache)
            except Exception as e:
                print(e)

            return render(
                request,
                "create/success.html",
                {
                    "schemaData": schemaData,
                    "propertyData": formset_instance,
                    "jsonResponse": data,
                },
            )

    return render(
        request,
        "create/create.html",
        {
            "schemaform": schemaform,
            "formset": formset,
        },
    )
