def insert_patient_data(name : str, age : int): # type hinting doesn't give errors
    if type(name) == str and (type(age) == int and age>0):
        print(name)
        print(age)
        print('inserted into database')
    else:
        raise TypeError('Incorrect Data Type')

def update_patient_data(name : str, age : int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError('Incorrect Data Type')

insert_patient_data('Robert',30)

# Pydantic class 
# 1.define ideal schema and validation constraints
# 2.Instantiate a object with that class 
# 3.Validated pydantic object passed to function

