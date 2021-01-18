![N|Solid](https://yt3.ggpht.com/ytc/AAUvwngTXEE_ZlhGUFxfLZWeNj4onBXUI7lVHvLwi0O1mQ=s900-c-k-c0x00ffffff-no-rj)
# Testsuperfuds

## Introduction:
The objective of this project is build an API REST to create a warehouse related to many descriptions. The project was created in django and django RestFramework. Two models was created, in a one to many relationship.

## Use:
This project isnt deployment yet, so you have to tested in localhost (see install). The following request are allowed:

### Warehouse model:
-  GET localhost:8000/warehouse // Brings all the warehouses with his descriptions asociated
-  GET localhost:8000/warehouse/ID // Brings a single warehouse by its id
-  POST localhost:8000/warehouse // Create a new warehouse with his descriptions asociated.
      Example:
```json
{
  "name":"warehouse1",
"headquartersNumber":1000,
"description":[
  {
      "phone":573456789,
      "city":"Bogota",
      "address":"Cr1 # 1-1"
  },
  {
      "phone":57341111,
      "city":"Bogota",
      "address":"Cr66 # 1-2"
  }
]
}
```
- PUT localhost:8000/warehouse/ID // Edit the warehouse by its id (given the whole object)
- PATCH localhost:8000/warehouse/ID // Edit the warehouse by its id (just given the fields to edit)
- DELETE localhost:8000/warehouse/ID // delete the warehouse by its id and all the description asociated

### Warehouse_description model:
-  GET localhost:8000/warehouse_description // Brings all the warehouses descriptions
-  GET localhost:8000/warehouse_description/ID // Brings a single warehouse by its id
-  POST localhost:8000/warehouse_description // Create a new warehouse description asociating the warehouse that belongs
      Example:
```json
{
    "phone":573456789,
    "city":"Bogota",
    "address":"Cr1 # 1-1",
    "warehouse_id":2
}
```
- PUT localhost:8000/warehouse_description/ID // Edit the warehouse description by its id (given the whole object)
- PATCH localhost:8000/warehouse_description/ID // Edit the warehouse description by its id (just given the fields to edit)
- DELETE localhost:8000/warehouse_description/ID // delete the warehouse description by its id 

## Install:
this project works with python 3.8
You need to instal django and django RestFramework and mysql client (to conect to rds database)
```sh
$ pip install django
$ pip install djangorestframework
pip install mysqlclient
```
Then, in the root of the project run the migrations with:
```sh
$ python manage.py migrate
```
And run the server:
```sh
$ python manage.py runserver
```
