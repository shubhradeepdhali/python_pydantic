from pydantic import BaseModel, EmailStr, AnyHttpUrl , Field
from typing import Optional, Annotated

# Field function - metadata and data constraints

# First create class
class Patient(BaseModel):
    name : Annotated[str, Field(max_length= 50, title = 'Name of patient', description='Enter patient name in less than 50 characters', examples=['Mohan','Aman'], default = None, strict = True)] # str = Field(max_length= 50)

    linkedIn : AnyHttpUrl | None = None
    age : int = Field(gt= 0, lt= 120)
    gender : str = 'Male'
    phone : int
    email : EmailStr | None = None # 'EmailStr' is Pydantic data type for checking email entries
    allergies : Optional[list[str]] = Field(max_length= 5) 
    address : dict[str,str]

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('inserted into database\n')


# patient_info = {'name':'Rahul','age':30}

# patient1 = Patient(**patient_info)

# insert_patient_data(patient1)

# updating patient data
def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.phone)
    print(patient.email)
    print(patient.allergies)
    print('details updated\n')

patient_info_2 = {'name': 'Shubhradeep','age': 25, 'gender' : 'M','email': 'abracadabra@gmail.com','phone': 8000,'allergies' : ['wheat','apple'], 'address':{'Sikkim':'Gangtok'}} 

patient2 = Patient(**patient_info_2)

update_patient_data(patient2)
