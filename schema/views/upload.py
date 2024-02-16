import pickle

from django.shortcuts import render, redirect

from ..models.schema import SchemaModel
from django.views.decorators.csrf import ensure_csrf_cookie
from ..functions.upload import (
    handleUploadFile,
    readValidateJson,
    querySchema,
    createMarkdown,
)
from ..functions.validators import validateUser
from ..functions.redisConnection import instantiateRedis, destroyRedis


@ensure_csrf_cookie
def upload(request):
    if request.method == "POST":

        handleUploadFile(request.FILES["uploadedFile"])
        data = readValidateJson(
            "static/" + str(request.FILES["uploadedFile"]),
            "Error reading the json file.",
        )

        try:
            cache = instantiateRedis()
            temp = cache.get("schema")
            schema = pickle.loads(temp)
            destroyRedis(cache)
        except Exception as e:
            print(e)

        schemaData = querySchema(request.POST.dict()["selectSchema"])
        flag, errors = validateUser(schemaData["properties"], data)
        if flag and len(errors) == 0:
            markdownContent = createMarkdown(data)
            return render(
                request, "upload/markdown.html", {"markdownContent": markdownContent}
            )
        else:
            return render(request, "upload/retry.html", {"errors": errors})

    return render(request, "upload/upload.html", {"details": SchemaModel.objects.all()})
