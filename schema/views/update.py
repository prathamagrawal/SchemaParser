from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from ..models.properties import PropertiesModel
from ..models.schema import SchemaModel
from ..forms.add import PropertiesFormset

def update(request):
    if(request.method == "POST"):
        formset = PropertiesFormset(request.POST)
        if formset.is_valid():
            formset_instance=formset.save(commit=False)
            for form in formset_instance:
                form.schemaDetails = SchemaModel.objects.filter(title=request.POST['selectSchema'])[0]
                form.save()
        return HttpResponse("Success")
    else:
        pass
    
    
    formset = PropertiesFormset(queryset=PropertiesModel.objects.none())
    return render(request,'update.html',{"details":SchemaModel.objects.all(),"formset":formset})