from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from ..models.properties import PropertiesModel
from ..models.schema import SchemaModel
from ..forms.add import PropertiesFormset


def modify(request):
    if request.method == "POST":
        """Delete Operation"""
        if request.POST["delete"]:
            selectedSchema = SchemaModel.objects.filter(
                title=request.GET.get("selectSchema", "")
            )[0]
            allProperties = PropertiesModel.objects.filter(schemaDetails=selectedSchema)
            propertyToDelete = request.POST.getlist("checks[]")
            for item in allProperties:
                if item.propertyTitle in propertyToDelete:
                    item.delete()

        "Add Operation"
        if request.POST["add"]:
            formset = PropertiesFormset(request.POST)
            if formset.is_valid():
                formset_instance = formset.save(commit=False)
                for form in formset_instance:
                    form.schemaDetails = SchemaModel.objects.filter(
                        title=request.GET.get("selectSchema", "")
                    )[0]
                    form.save()

        schemaData = SchemaModel.objects.filter(
            title=request.GET.get("selectSchema", "")
        )[0]
        allProperties = PropertiesModel.objects.filter(
            schemaDetails=schemaData
        ).values()

        if request.POST["add"] == "yes":
            return render(
                request,
                "update/updatedSchema.html",
                {
                    "schemaData": schemaData,
                    "propertyData": allProperties,
                    "message": "Only Add operation were made!",
                },
            )
        elif request.POST["delete"] == "yes":
            return render(
                request,
                "update/updatedSchema.html",
                {
                    "schemaData": schemaData,
                    "propertyData": allProperties,
                    "message": "Only delete operation were made!",
                },
            )
        elif request.POST["add"] == "yes" and request.POST["delete"] == "yes":
            return render(
                request,
                "update/updatedSchema.html",
                {
                    "schemaData": schemaData,
                    "propertyData": allProperties,
                    "message": "Both add and delete operation were made!",
                },
            )
        else:
            return render(
                request,
                "update/updatedSchema.html",
                {
                    "schemaData": schemaData,
                    "propertyData": allProperties,
                    "message": "No Changes were carried out.",
                },
            )

    else:
        formset = PropertiesFormset(queryset=PropertiesModel.objects.none())
        selectedSchema = SchemaModel.objects.filter(
            title=request.GET.get("selectSchema", "")
        )
        selectedProperties = PropertiesModel.objects.filter(
            schemaDetails=selectedSchema[0]
        ).values()
        return render(
            request,
            "update/update.html",
            {
                "selectSchema": request.GET.get("selectSchema", ""),
                "formset": formset,
                "selectedProperties": selectedProperties,
            },
        )


def selectSchema(request):
    if request.method == "POST":
        return redirect("/modify/?selectSchema={}".format(request.POST["selectSchema"]))

    return render(
        request, "update/selectSchema.html", {"details": SchemaModel.objects.all()}
    )
