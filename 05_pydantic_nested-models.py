from pydantic import BaseModel

class Address(BaseModel):
    city :str
    state : str
    pin : int

class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address : Address

address_dict = {'city': 'Gurgaon', 'state': 'Haryana', 'pin': 678887}
address_01 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address_01}
patient_01 = Patient(**patient_dict)

temp = patient_01.model_dump
print(temp)