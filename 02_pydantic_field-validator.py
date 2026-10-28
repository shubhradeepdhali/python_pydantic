from pydantic import BaseModel, EmailStr, AnyHttpUrl , Field , field_validator
from typing import Optional, Annotated

# First create class
class Patient(BaseModel):
    
    name : Annotated[str, Field(max_length = 50, min_length= 5, title='Enter patient name', description= 'Enter the name of patient , minimum 5 characters and maximum 50 characters') ]
    age : Annotated[int ,Field (gt = 0, lt = 120) ]
    phone : int | None = None
    email : EmailStr
    allergies : list[str] = Field (max_length= 5)
    married : bool = Field (default = False)


    # using field validators using function decorators
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com',"sbi.com"]
        domain_name = value.split('@')[-1] # '.split' returns a list
        if domain_name not in valid_domains:
            raise ValueError('Employee not eligible for reimbursements') # 'raise' interrupts and exits the function just like return
        return  value

    @field_validator('age')
    @classmethod
    def age_validator(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Invalid age')

    # using field validator to transform values
    @field_validator('name')
    @classmethod
    def name_transformer(cls, value):
        return value.upper()


def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.phone)
    print(patient.email)
    print(patient.allergies)
    print(patient.married)
    print('details updated\n')

patient_info_01 = {'name':'Rahul', 'phone': 9900499005, 'age': 50, 'email': 'rahul@hdfc.com', 'allergies': ['wheat', 'onion']}

patient_01 = Patient(**patient_info_01) # instantiating the Patient class

update_patient_data(patient= patient_01)