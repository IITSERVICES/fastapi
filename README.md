
## Module 3 – FastAPI + REST APIs

- FastAPI Introduction
- Project Setup
- Routes and Endpoints
- Path Parameters
- Query Parameters
- Request Body
- Pydantic Models
- Response Models
- CRUD REST APIs
- Dependency Injection
- Authentication
- JWT Authentication
- Middleware
- Exception Handling
- API Documentation – Swagger/OpenAPI
- Database Integration
- FastAPI Project

##What is FastAPI?

FastAPI is a Python framework for developing REST APIs and backend services.
For GenAI applications, we commonly need a backend like:
```
Angular / React
       ↓
    FastAPI
       ↓
 ┌─────┼─────────┐
 ↓             ↓                       ↓
 LLM     RAG                Database
 API      System
```

## Example:
```
POST /chat
POST /documents
GET  /documents
POST /search
POST /agents

Note : The frontend doesn't directly need to communicate with the LLM.
```
##Instead of
 ```
 Angular -> FastAPI -> AI Services -> LLM
```

This is much closer to how an enterprise application is designed.

1. Create our first FastAPI application
Create a folder:
```
genai-training/
    fastapi-basics/
```
Inside it:
```
fastapi-basics/
│
├── app/
│   └── main.py
│
└── requirements.txt
```
### Why Should We Create a Virtual Environment (venv) in a Python Project?

1. What is a Virtual Environment?
A virtual environment is an isolated environment created specifically for a Python project. It allows the project to have its own Python packages and package versions, without affecting other Python projects on the same computer.

In simple words:

venv creates a separate room for each Python project where that project can keep its own required libraries.

## For example, suppose you have two projects:
```
Project A requires Django 4.2
Project B requires Django 5.2
```
If both projects use the same global Python environment, installing one version may create conflicts. With venv, each project can use its own version safely.
## Main Advantages of venv
① Avoid Package Version Conflicts
Different projects may require different versions of the same library.

## For example:
```
Project A → Django 4.2
Project B → Django 5.2
```

Using separate virtual environments allows both projects to work correctly.
Keeps the Global Python Clean

Without venv, we may install many packages globally:
```
pip install django
pip install numpy
pip install pandas
pip install flask
```
After working on many projects, the global environment becomes difficult to manage.
With venv, packages are installed inside the project environment.

Project Independence
Each project gets its own dependencies.

##For example:
```
StudentManagement
   └── venv
       ├── Django
       └── mysqlclient

AIChatbot
   └── venv
       ├── LangChain
       ├── OpenAI
       └── NumPy
```
Changing packages in one project does not normally affect the other.

Easy Dependency Management
We can save the packages required by a project in:
requirements.txt
##For example:
```
Django==5.2
numpy==2.2.0
pandas==2.2.3
```
Another developer or student can create a virtual environment and install the same dependencies:
```
pip install -r requirements.txt
```

This helps make the project reproducible.
##Step1:
```
python -m venv venv
```
## Activate on windows
```
venv\Scripts\activate
```
Now install fastapi and uvicorn
```
python -m pip install fastapi uvicorn
```
##Step2: 
```
pip install -r requirements.txt
```
##Step3: create main.py
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to GenAI Backend Training"
    }

```
##Step4:
```
uvicorn app.main:app --reload
```
##Project Structure
```
#---------------------------------------------------
# In order to execute we use the following command
```

```
uvicorn app.employee:app --reload
```

# In order to test all the endspoint with swagger we can use the following URL

```

http://127.0.0.1:8000/docs
```
