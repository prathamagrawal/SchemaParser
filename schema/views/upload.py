from django.shortcuts import render,redirect
from ..models.schema import SchemaModel
from django.views.decorators.csrf import ensure_csrf_cookie
from ..functions.upload import handleUploadFile,readValidateJson,querySchema,createMarkdown
from ..functions.validators import validateUser


@ensure_csrf_cookie
def upload(request):
    if request.method=='POST':
        
        handleUploadFile(request.FILES['uploadedFile'])
        data=readValidateJson("static/"+str(request.FILES['uploadedFile']),"Error reading the json file.")
        schemaData=querySchema(request.POST.dict()['selectSchema'])
        flag,errors=validateUser(schemaData['properties'],data)
        if(flag and len(errors)==0):
            markdownContent=createMarkdown(data) 
            return render(request,'markdown.html',{'markdownContent':markdownContent}) #TODO: Make the html pages for success and retry.
        else:
            return render(request,'retry.html',{'errors':errors})
    
    return render(request,'upload.html',{"details":SchemaModel.objects.all()})


