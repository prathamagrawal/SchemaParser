<h1 align="center">Schema Parser</h1>
<img width="1376" alt="Screenshot 2024-02-13 at 11 41 52" src="https://github.com/prathamagrawal/JsonSchemaAPI/assets/58286330/a089e296-d1d4-4440-95d6-71a6d4b15ecf">

## Description 📍
This tool provides a user-friendly interface powered by Django for managing JSON schemas, validating JSON responses, and generating documentation. With features for adding, updating, and validating schemas, users can efficiently work with JSON data.

<hr>

## Following are the project features: 📍

1. Add Schema:

<ul>
<li>Allow users to add a new JSON schema to the tool.</li>
<li>Validate the added schema for correctness.</li>
<li>Provide feedback on successful addition or errors in the new schema.</li>
</ul>

2. Create Documentation (with Internal Schema Validation):
<ul>
<li>Generate human-readable documentation from a selected JSON schema.</li>
<li>Internally validate the provided schema to ensure its correctness.</li>
<li>Display detailed error messages if the schema is invalid. </li>
<li>Save documentation to a file or display it on the console.</li>
</ul>

3. Update Schema:
<ul>
<li>Enable users to update an existing JSON schema.</li>
<li>Validate the updated schema for correctness.</li>
<li>Allow operations such as adding, modifying, or removing properties and constraints.</li>
<li>Provide feedback on the success of the update or errors in the updated schema.</li>
</ul>

<hr>

## Setup 🚀
### Prerequisites:
Make sure python3.9 is installed. Check the version of the python installed using 
```
python --version
```

Steps to get the application running:
1. Clone the repository:
   ```
   git clone https://github.com/prathamagrawal/SchemaParser.git
   cd SchemaParser
   ```
2. Install requirements.txt
   ```
   pip install -r requirements.txt
   ```
3. Make Migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```  
4. Collect the static files
   ```
   python manage.py collectstatic
   ```
5. Create Superuser
   ```
   python manage.py createsuperuser
   ```
6. Run the server
   ```
   python manage.py runserver
   ```


<hr>

## Usage 📍

### 1. Schema Creation
A user can create a schema using the add schema option. Multiple properties can be added and removed. Customizations can be made for their respective datatypes and whether they are used or not.

#### Creation 
<img width="1440" alt="Screenshot 2024-02-13 at 11 50 40" src="https://github.com/prathamagrawal/JsonSchemaAPI/assets/58286330/0653f1af-d5e2-478b-85a0-18393e9d72e9">

#### View and Download Schema as json
<img width="1440" alt="Screenshot 2024-02-13 at 11 51 47" src="https://github.com/prathamagrawal/JsonSchemaAPI/assets/58286330/49844b50-6d84-474d-9427-55f12884cdf1">

The following schema can be downloaded as json: 

```
{
    "title": "employee database",
    "description": "Information of all employees",
    "properties": [
        {
            "propertyTitle": "Name",
            "propertyDescription": "Name of the employee",
            "propertyDataType": "str",
            "propertyRequired": false
        }
    ]
}
```

### 2. Validation and Creation of Readme 
A user can select schema and upload a json file. The file would be validated against the json schema, if it passes it would convert it into a markdown file. If not, it would log the errors to the user. 

#### Select Schema and Upload file
<img width="1440" alt="Screenshot 2024-02-13 at 11 57 35" src="https://github.com/prathamagrawal/JsonSchemaAPI/assets/58286330/9827022c-3373-4242-95a9-b9e229c900dd">

#### Validation Successful
<img width="1440" alt="Screenshot 2024-02-13 at 12 00 42" src="https://github.com/prathamagrawal/JsonSchemaAPI/assets/58286330/5a3fe556-ed47-4ada-b071-e6bd1857acac">

#### Validation Failed
<img width="1440" alt="Screenshot 2024-02-13 at 12 01 08" src="https://github.com/prathamagrawal/JsonSchemaAPI/assets/58286330/a6e6aee7-98d6-49e7-b61f-386a6e166356">

### 3. Update Schema
A user can add or delete properties in a schema, and later the final updated schema can be viewed as well as download. 

#### Add Properties
<img width="1440" alt="Screenshot 2024-02-13 at 12 03 50" src="https://github.com/prathamagrawal/JsonSchemaAPI/assets/58286330/4a3d7382-d987-42d0-b8e7-36e279993f39">

#### Delete Properties
<img width="1440" alt="Screenshot 2024-02-13 at 12 04 41" src="https://github.com/prathamagrawal/JsonSchemaAPI/assets/58286330/97620dfe-c21c-409e-aba6-f3684b33d1e2">

<hr>
