# Python Pydantic Fundamentals

This repository covers the fundamentals of **Pydantic**, a Python library used to validate, parse, and serialize data using type hints. It helps ensure that incoming data follows the structure and rules defined by your Python models.

## What Is Pydantic?

Pydantic uses Python type annotations to validate data at runtime. It is commonly used to validate API requests and responses, configuration settings, and structured data from JSON or other sources.

Unlike a regular Python class, a Pydantic model validates the values supplied when an instance is created. Depending on the field type and configuration, Pydantic may also convert compatible input values to the declared type.

This repository focuses on **Pydantic v2**.

## Topics Covered

### 1. Pydantic Classes (Models)

Pydantic models are created by inheriting from `BaseModel`. Their annotated attributes define the fields and expected data types.

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

patient = Patient(name="Asha", age=25)
print(patient.name)  # Asha
```

When a model is instantiated, Pydantic validates the provided data against the model's field definitions.

### 2. Field Validation — `@field_validator`

A field validator lets you add custom validation or processing for one or more specific fields. Use `@field_validator` when a rule applies to an individual field, such as checking a value or normalizing text.

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def username_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Username cannot be blank")
        return value.strip()
```

Pydantic also provides `Field(...)` for built-in constraints such as minimum length, maximum length, and numeric bounds.

### 3. Model Validation — `@model_validator`

A model validator is useful when validation depends on multiple fields or on the model as a whole. For example, it can check that a start date comes before an end date, or that two fields are consistent with each other.

In Pydantic v2, model validators commonly use `mode="after"` to validate the constructed model or `mode="before"` to inspect the input data before field validation.

```python
from pydantic import BaseModel, model_validator

class Booking(BaseModel):
    start: int
    end: int

    @model_validator(mode="after")
    def check_range(self):
        if self.end < self.start:
            raise ValueError("end must be greater than or equal to start")
        return self
```

### 4. Computed Fields — `@computed_field`

A computed field exposes a value calculated from other model attributes. It is useful for derived values, such as a full name or total price. Computed fields are included in serialization by default.

```python
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

rectangle = Rectangle(width=4, height=3)
print(rectangle.area)  # 12.0
print(rectangle.model_dump())
```

A computed field is not the same as an input field: its value is derived from the model rather than supplied as an ordinary field during initialization.

### 5. Nested Models

Nested models let a model contain another Pydantic model as a field. They are useful for representing structured data with multiple levels, such as a patient with an address or an order containing several products.

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    postal_code: str

class Customer(BaseModel):
    name: str
    address: Address

customer = Customer(
    name="Asha",
    address={"city": "Kolkata", "postal_code": "700001"},
)

print(customer.address.city)  # Kolkata
```

Pydantic validates the nested data against the `Address` model as well as validating the outer `Customer` model.

### 6. Serialization

Serialization converts a Pydantic model into formats that are convenient for storage, APIs, or data exchange.

Common methods in Pydantic v2 include:

- `model_dump()` — converts a model into a Python dictionary.
- `model_dump_json()` — converts a model into a JSON string.
- `model_validate(data)` — validates data and creates a model instance.
- `model_validate_json(json_data)` — validates JSON data and creates a model instance.

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float

product = Product(name="Keyboard", price=49.99)

python_data = product.model_dump()
json_data = product.model_dump_json()

print(python_data)
print(json_data)
```

Serialization is the conversion of a model into an output representation; validation is the process of checking and parsing input data.

## Installation

Install Pydantic with pip:

```bash
pip install pydantic
```

Some email-related types, such as `EmailStr`, require the optional email validation dependency:

```bash
pip install "pydantic[email]"
```

## Learning Goals

By working through these topics, you will learn how to:

- Define structured data models using Python type hints.
- Apply built-in field constraints and custom field validation.
- Validate rules that depend on multiple fields.
- Create derived values with computed fields.
- Represent complex data using nested models.
- Convert models to dictionaries and JSON, and validate data from those formats.

## Resources

- [Official Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic Validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [Pydantic Serialization](https://docs.pydantic.dev/latest/concepts/serialization/)
