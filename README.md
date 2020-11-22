# Ukufu Tech Task

## Problem Statement

A set of reciepes and Ingredients are given, build Rest API, which should determine and 
return all possible recipes with fresh Ingredients (not expired). 

### Problem Analysis

Though the problem looks like a simple REST API implementation, the business logic has greater scope for extention.
It is a variation of Donald Knuth's Algorithm X, Exact Cover, Max Cover with optimization for max recipes and min recipes.

https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X. Due to time constraints from my side, I would love to discuss this in the
later discussions.

To submit the solution in time, a minimalistic apparoach has been taken.

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

### Running the Solution

__Note:__ docker required

Clone git repository: https://github.com/narenallam/ukufu.git and change directory to ukufu. (or)

Simply download 'docker-composer.yml' file from the same repository (above ).

run the following command, where the 'docker-composer.yml' exists.

```bash
$ docker-composer up
```

Now solutions is downloaded and running...

### Summary

Functionally the problem is divided into two REST API services, running in docker containers,

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

### API usage

When both the services are running, we should see the below screen at http://127.0.0.1:8000/lunch/, 

<img src="https://github.com/narenallam/ukufu/blob/master/ukufu/images/Capture7.PNG" width=400>

click on Try it out button

<img src="https://github.com/narenallam/ukufu/blob/master/ukufu/images/Capture4.PNG" width=400>

Click Execute button and we can see output there itself

<img src="https://github.com/narenallam/ukufu/blob/master/ukufu/images/Capture5.PNG" width=400>

The above output is for current date (today), we can also pass custom date, using another API, click on the API as shown below

<img src="https://github.com/narenallam/ukufu/blob/master/ukufu/images/Capture8.PNG" width=400>

Enter date: 2021-3-26 as shown below


<img src="https://github.com/narenallam/ukufu/blob/master/ukufu/images/Capture6.PNG" width=400>

As swagger API documetation is built, most of the API from Data Manger API or Lunch Manger API are self explanatory.

### Technolgy used

__Platform__

* Ubuntu 20.04 LTS
* Mac OS X BigSur
* Windows 10 Workstation with WSL2
* docker
* python 3.8.5 and 3.9

__Python Libraries Used__

* flask: For res API
* flask-restplus: For swagger
* json: JSON parsing
* pickle: in-memory data backup
* urllib3: cross service communication
* logging: for app specific rotating file logger
* unitest: for integration and unitests
* mock: for unittesting
* pylint: PEP8 compliance

__Tools used__

* git
* docker and docker-composer
* vscode
   
### Running the services from source

__Python version >= 3.8.5 required, on ubuntu (18.04/20.04)__

```bash
sudo apt install python3.8.5
```
__Pull the code from git repository__

```bash
user@host:~/$ git clone https://github.com/narenallam/ukufu.git
```
__Change directory to Tasks__

```bash
user@host:~/$ cd ukufu
```
__Creating Virtual environment__

```bash
user@host:~/ukufu$ sudo apt-get install python3-pip

user@host:~/ukufu$ pip3 install virtualenv

user@host:~/ukufu$ virtualenv -p python3.8.5 venv

user@host:~/ukufu$ source venv/bin/activate

(venv) user@host:~/ukufu$  pip install -r ukufu/lunch_api/requirements.txt
```

__Run Data Manger API__

```bash
# Make sure that we are inside first ukufu folder
(venv) user@host:~/ukufu$ cd ukufu/db_api
(venv) user@host:~/ukufu/ukufu/db_api$ python -m src.data_api
```

We Should see the below screen at http://127.0.0.1:5000

<img src="https://github.com/narenallam/ukufu/blob/master/ukufu/images/Capture1.PNG" width=400>

__Run Lunch Manger API__

```bash
# Make sure that we are inside first ukufu folder
(venv) user@host:~/ukufu$ cd ukufu/lunch_api
(venv) user@host:~/ukufu/ukufu/lunch_api$  python -m src.lunch_api
```

We Should see the below screen at http://127.0.0.1:8000

 <img src="https://github.com/narenallam/ukufu/blob/master/ukufu/images/Capture2.PNG" width=400>
 
__Running Integration tests__

```bash
# Make sure that we are inside first ukufu folder
(venv) user@host:~/ukufu$ cd ukufu/lunch_api
(venv) user@host:~/ukufu/ukufu/lunch_api$ python -m tests.int_tests
```
We should see the below out put in the terminal

 <img src="https://github.com/narenallam/ukufu/blob/master/ukufu/images/Capture3.PNG" width=400>

__Running unit tests__

```bash
# Make sure that we are inside first ukufu folder
(venv) user@host:~/ukufu$ cd ukufu/db_api
(venv) user@host:~/ukufu/ukufu/lunch_api$ python -m tests.unit_tests

