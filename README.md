# Ukufu Tech Task

## Problem Statement

A set of reciepes and Ingredients are given, build Rest API, which should determine and 
return all possible recipes with fresh Ingredients (not expired). 

#### User Story

As a User I would like to make a request to an API that will determine from a set of recipes what I can
have for lunch today based on the contents of my fridge so that I quickly decide what I’ll be having.

#### Acceptance Criteria

* Given that I have made a request to the /lunch endpoint I should receive a JSON response of
the recipes that I can prepare based on the availability of ingredients in my fridge
* Given that an ingredient is past its use-by date, I should not receive recipes containing this
ingredient
* Given that an ingredient is past its best-before date, but is still within its use-by date, any
recipe containing this ingredient should be sorted to the bottom of the response object

#### Additional Criteria

* The application SHOULD contain some basic unit / integration tests (e.g. using PHPUnit, JUnit,
Uni est )
*  The applica on MUST be completed using an OOP approach
* The application MUST be enforce code-style (e.g. PSR, PEP 8, Checkstyle, Stylecop)
* Any dependencies MUST be installed using a package manager (no need to commit
dependencies, e.g. Composer, PIP, Nuget )
* Use a rela vely new release of the version
* Any installation on, build steps, testing and usage instructions MUST be provided in a README.md
file in the root of the application

<Hr>
   
## Solution

Functionally the problem is divided into two REST API services, 

1. Data Manager API - Which takes care of all data loading/backup/reloading and CRUD operations on entities like Recipe and Ingredients.
   This works like an adaptor for other services and backend can be easily replaced with any Database. Running at http://127.0.0.1:5000.
   
2. Lunch Manager API - Which serves the core business logic, initially fecthes data from 'Data Manger API' and runs at http://127.0.0.1:8000.

3. Once Both the services are running, open http://127.0.0.1:8000/lunch/,  we should should see the following output

```json
{
    "menu": [
        "Ham and Cheese Toastie",
        "Salad",
        "Hotdog"
    ]
}
```
   
### Running the services from source

__Python version 3.8.5 required, on ubuntu (18.04/20.04)__

```bash
sudo apt install python3.8.5
```
__Pull the code from git repository__

```bash
user@host:~/$ git clone https://github.com/narenallam/Tasks.git
```
__Change directory to Tasks__

```bash
user@host:~/$ cd Tasks
```
__Creating Virtual environment__

```bash
user@host:~/Tasks$ sudo apt-get install python3-pip

user@host:~/Tasks$ pip3 install virtualenv

user@host:~/Tasks$ virtualenv -p python3.8.5 venv

user@host:~/Tasks$ source venv/bin/activate

(venv) user@host:~/Tasks$  pip install -r requirements.txt
```

__Run Data Manger API__

```bash
# Make sure that we are inside Tasks folder
(venv) user@host:~/Tasks$  python -m Src.data_api
```

We Should see the below screen at http://127.0.0.1:5000

<img src="https://github.com/narenallam/Tasks/blob/master/Images/Capture1.PNG" width=400>

__Run Lunch Manger API__

```bash
# Make sure that we are inside Tasks folder
(venv) user@host:~/Tasks$  python -m Src.lunch_api
```

We Should see the below screen at http://127.0.0.1:8000

 <img src="https://github.com/narenallam/Tasks/blob/master/Images/Capture2.PNG" width=400>
 
__Running Integration tests__

```bash
# Make sure that we are inside Tasks folder
(venv) user@host:~/Tasks$ python -m Tests.int_tests
```

We Should see the below output in terminal

 <img src="https://github.com/narenallam/Tasks/blob/master/Images/Capture3.PNG" width=600>
