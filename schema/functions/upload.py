import os
import json
from ..models.schema import SchemaModel
from ..models.properties import PropertiesModel


def handleUploadFile(file):  
    static_folder = 'static/' 
    os.makedirs(static_folder, exist_ok=True)
    with open(os.path.join(static_folder, file.name), 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def readValidateJson(inFile,message):
    with open(inFile) as file:    
        try:
            return json.load(file) 
        except json.decoder.JSONDecodeError:
            print(message) 
            return {}
        

def querySchema(name):
        selectedSchema=SchemaModel.objects.filter(title=name)
        propertiesQuery=PropertiesModel.objects.filter(schemaDetails=selectedSchema[0]).values()
        data=list(selectedSchema.values())[0]
        properties = [{key: value for key, value in item.items() if key not in ['id', 'schemaDetails_id']} for item in propertiesQuery]
        data['properties']={item['propertyTitle']: item for item in properties}
        return data


def createMarkdown(data,outFile="output.md"):

        markdownContent=""""""
        markdownContent+="# MarkDown File: \n\n"

        try:
            for key,value in data.items():
                if(type(value)!=dict):
                    markdownContent+=f"## {key} : {value} \n"
                    markdownContent+="\n"
                else:
                    markdownContent+=f"## {key}: \n"
                    for item,itemValue in value.items():
                        markdownContent += f"   -**{item}**: {itemValue} \n"
                        markdownContent+="\n"
            try:
                # with open(outFile, 'w') as file:
                #     file.write(markdownContent)
                    print("Successfully wrote the Markdown!")
                    return markdownContent
            except:
                print("Error while writing to Output.md")
        except:
            print("Failed!")