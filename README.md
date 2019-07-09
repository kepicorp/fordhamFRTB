# Fordham FRTB Project

> Documentation v1.1
> 4th July 2019

## Running the system

### Creating an ngrok account

1. Go to [ngrok website](https://ngrok.com/) and create a free acount.
2. Access your [dashboard](https://dashboard.ngrok.com/) and save or take note of your *token* defined in the box labelled 3.
3. Check in the [dashboard](https://dashboard.ngrok.com/) the status of current connections.

> We are going to use *ngrok* to allow your program to be visible from the outside world. Usually when you run something on your computer it is protected from being accessible from anywhere around.

### Starting the project

First let's construct the images that we are going to need to test the system.
For this we will go to the project directory and execute:

```
docker-compose build
```

When done the images should be ready.
Simply run

```
docker-compose up
```

To start your system.

When you want to shutdown press *Ctrl+C* on your keyboard.

### Web Server Methods

Endpoint accessible on your web server on port 5000
* [Server Status](http://localhost:5000), this will give you the default *token* if logged already
* [Test my project](http://localhost:5000/compute)
* [Log out from Back-end](http://localhost:5000/logout)
* [Log in to Back-end](http://localhost:5000/login), this should be called automatically when testing your project
* [List existing cubes](http://localhost:5000/cube)
* [List existing reports](http://localhost:5000/reports)
* [The end point to use in node-red](http://localhost:5000/computered)

## Excercise to do

### Create the financial library

Implement the ```def compute()``` method in the ```financial.py``` file in your flask app

> Be carfeful the file must give back a csv string that look like the following
> PK indicute the primary key, unique identifier for the row
> The second line is the type could be *string* or *double*

| Column1:PK | column 2 | column 3 |
| --- | --- | --- |
| string | string | double |
| A1 | B1 | 12 |
| A2 | B2 | 24 |

In a python string this would look like:
```python
csvOutput = "Column1:PL;Column2;Column3\nstring;string;double\nA1;B1;12\nA2;B2;24"
```

> Please note the usage of *\n* for return to next line and *;* as a separator.

### Configuration

All configuration paramaters are available in ```config.py``` file including:
* Name of the report you want to create for UXP
* Endpoint you are using for connectivity

