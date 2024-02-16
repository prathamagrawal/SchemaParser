def validateUser(schema,data):
    data={key.lower(): value for key, value in data.items()}
    errors=[]
    isValid=True
    for key,value in schema.items():
        if(key not in data.keys() and (schema[key]['propertyRequired'])):
            errors.append(f"{key} not found")
            isValid=False

        if(key in data.keys()) and (schema[key]['propertyDataType']=="int" and type(data[key])!=int):
            errors.append(f"{key} is not suited for integer")
            isValid=False

        if(key in data.keys()) and (schema[key]['propertyDataType']=="string" and type(data[key])!=str):
            errors.append(f"{key} is not suited for integer")
            isValid=False


    for key in data.keys():
        if(key not in schema.keys()):
            isValid=False
            errors.append(f"{key} is not in schema!")
    
    return isValid,errors