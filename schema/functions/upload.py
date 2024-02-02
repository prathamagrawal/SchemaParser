import os

def handleUploadFile(file):  
    static_folder = 'static/' 
    os.makedirs(static_folder, exist_ok=True)
    with open(os.path.join(static_folder, file.name), 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)