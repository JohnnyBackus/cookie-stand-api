# LAB - Class 34

## Project: Putting it All Together

### Author: Johnny Backus

### Links and Resources

- [CodeFellows Python Lab Instructions](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/)
- [CodeFellows README template](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/README-template.html)
- lecture demo code used for reference

### Setup

- *.env requirements: n/a*

### How to Initialize/Run Your Application

- activate virtual environment
- pip install -r requirements.txt
- enter CLI command python manage.py runserver
- path to cookiestand_list is http://127.0.0.1:8000/cookiestands/

### How to Use Your Library

- n/a

### Tests

#### How to Run Tests

- `python manage.py test`

#### Tests of Note

- used APITestCase for CRUD
- Able to perform all functions from admin page

#### Incomplete Tests

- cookiestands created on user facing site did not persist.
- updates to cookiestands on user facing site did not persist.
- when running pytest, received error: "Got an error creating the test database: permission denied to create database"
