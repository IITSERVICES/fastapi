from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app  = FastAPI(title='EMPLOYEE CRUD OPERATIONS')

#-----------------
# EMPLOYEE CRUD OPERATIONS
#----------------

# Pydantic Model
# It is used to declare the type so that we can use any were

class Employee(BaseModel):
    eid:int
    ename:str
    esalary:float
    department:str

#------------------
# In Memory-Data based
#------------------
employees=[
    Employee(eid=1001,ename='IMTIAZ',esalary=40000.0,department='IT'),
    Employee(eid=1002,ename='AR',esalary=50000.00,department='HR')
]

# Now Create the End Points
#------------------------------------------------------------------

#1.  GET : Get All the Employees
#Endpoint : GET http://localhost:8000/employees

@app.get("/employees",summary='GET ALL EMPLOYEES')
def getAllEmployees():
    return employees

#2. GET : Get the specific employee based on eid
# Endpoint : GET http://localhost:8000/employees/1001
@app.get("/employees/{eid}",summary='GET THE EMPLOYEE BY EID')
def getEmployeeById(eid:int):
    for employee in employees:
        if employee.eid ==eid:
            return employee
    raise HTTPException(
        status_code=404,
        detail="Employee Not Found"
    )


#3. Create an Employee 
#Endpoint : POST  http://localhost:8000/employees
@app.post("/employees",summary='CREATE THE EMPLOYEE')
def createEmployee(employee:Employee):
    for emp in employees:
        if emp.eid == employee.eid:
            raise HTTPException(
                status_code=400,
                detail='Employee Already Exists'
            )
    employees.append(employee)
    return{
        "message":"Employee Created Succesfully",
        "employees":employee
    }

#4. Update : Update a specific employee details
#Endpoint  : PUT  http://localhost:8000/employees/1001
#---------------
#  {
#  eid:1001,
#  ename:"Imtiaz",
#  esalary:90000.00,
#  department:"IT"
#  }
#----------------

@app.put("/employees/{eid}",summary='UPDATED BY EMPLOYEE EID')
def updateEmployeeById(eid:int,employee:Employee):
    for index, emp in enumerate(employees):
        if emp.eid==eid:
            employees[index]=employee
            return{
                "message":"Employee Updated Successfully",
                "employee":employee
            }
    raise HTTPException(
        status_code=404,
        detail="Employee Not Found"
    )

#5. Delete : Delete the employee by eid
#Endpoint : DELETE http://localhost:8000/employees/1003
@app.delete("/employees/{eid}",summary="DELETE BY EMPLOYEE EID")
def deleteEmployeeByEid(eid:int):
    for index,emp in enumerate(employees):
        if emp.eid ==eid:
            delete_employee=employees.pop(index)
            return{
                "message":"Employee Deleted Successfully",
                "employee":delete_employee
            }
    raise HTTPException(
        status_code=404,
        detail="Employee Not Found"
    )
            
