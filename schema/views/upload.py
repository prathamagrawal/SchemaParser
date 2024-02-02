from django.shortcuts import render
from ..models.schema import SchemaModel
from django.views.decorators.csrf import ensure_csrf_cookie
from ..functions.upload import handleUploadFile


@ensure_csrf_cookie
def upload(request):
    if request.method=='POST':
        selectedSchema=request.POST.dict()['selectSchema']
        print(selectedSchema)
        handleUploadFile(request.FILES['uploadedFile'])
        

        return render(request,'base.html')
    return render(request,'upload.html',{"details":SchemaModel.objects.all()})
