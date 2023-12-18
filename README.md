# crud-postgre-django
### This application made with django rest_framework API.

## Setup
First thing you need before running application:
Make sure to do database migrations first.
- To migrate database you can run this script inside django_restapi folder with python or python3
```
python manage.py makemigrations
```
- After creating migration folder, run script
```
python manage.py migrate
```
- Then create superuser for your access
```
python manage.py createsuperuser
```
Fill all data and migration will be completed.

#### You can disable authentication by comment :
`employee/api/router.py`
```
# permission_classes = [permissions.IsAuthenticated]
```

## Running program
You can run program with `terminal` with python or python3
- For Python3 you can run with
```
python3 manage.py runserver
```
or with python
```
python manage.py runserver
```

## List Api URL
#### Access admin authentication
```http
  GET localhost:8000/admin
```
#### Access all employee
```http
  GET localhost:8000/api/employee
```
#### Get employee by id
```http
  GET localhost:8000/api/employee/{id_employee}
```
#### Add new employee
```http
  POST localhost:8000/api/employee/
```
With parameter<br/>
`{
    "id_employee": "",
    "fullname": "",
    "address": "",
    "mobile": "",
    "email": "",
    "position": "",
    "user": null
}`
#### Update data of employee by id
```http
  PUT localhost:8000/api/employee/{id_employee}
```
With parameter<br/>
`{
    "fullname": "",
    "address": "",
    "mobile": "",
    "email": "",
    "position": "",
    "user": null
}`
#### Delete employee by id
```http
  DELETE localhost:8000/api/employee/{id_employee}
```