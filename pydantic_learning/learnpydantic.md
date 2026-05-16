````md
# Pydantic Basics

## What is Pydantic?

:contentReference[oaicite:0]{index=0} is a Python library used for data validation and parsing using Python type hints.

It helps:
- Validate data
- Convert data types automatically
- Create clean and safe models

---

# Example

```python
from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool=False

input_data={"id":10,"name":"nikita","is_active":True}

user=User(**input_data)

print(user)
````

---

# What Happens Here?

* `BaseModel` creates a data model
* `id:int` means id must be integer
* `name:str` means name must be string
* `is_active:bool=False` gives a default value

Pydantic checks and validates data automatically.

---

# Output

```python
id=10 name='nikita' is_active=True
```

---

# Features of Pydantic

* Automatic validation
* Type conversion
* Default values
* Cleaner code
* Useful in APIs and backend development

---

# Example of Type Conversion

```python
User(id="10",name="nikita")
```

Pydantic converts `"10"` into integer `10`.

---

# Why Use Pydantic?

Without Pydantic:

* Manual checking is needed

With Pydantic:

* Validation is automatic
* Code becomes safer and professional

---

# Commonly Used With

* FastAPI
* AI/ML projects
* APIs
* Backend systems

```
```
````md id="8nbq4p"
# Pydantic Fields & Types Notes

## Fields in Pydantic

Fields are variables inside a model.

Example:

```python
class User(BaseModel):
    name: str
    age: int
````

* `name` → field
* `age` → field

---

# Type Annotations

Pydantic uses type annotations for validation.

Syntax:

```python
field_name: type
```

Example:

```python
id: int
name: str
price: float
is_active: bool
```

---

# Common Types

| Type    | Meaning        |
| ------- | -------------- |
| `str`   | String/Text    |
| `int`   | Integer        |
| `float` | Decimal Number |
| `bool`  | True/False     |

---

# List Type

```python
items: List[str]
```

Meaning:

* items must be a list
* every item must be string

Example:

```python
["apple", "banana"]
```

Import:

```python
from typing import List
```

---

# Dictionary Type

```python
value: Dict[str, int]
```

Meaning:

* key → string
* value → integer

Example:

```python
{"love": 1}
```

Import:

```python
from typing import Dict
```

---

# Optional Fields

```python
images: Optional[list] = None
```

Meaning:

* field can have value
* or can be None

Import:

```python
from typing import Optional
```

---

# Default Values

```python
is_active: bool = False
```

If user does not provide value:

* default value is used

---

# Object Creation

## Correct

```python
user = User(name="nikita", age=20)
```

## Wrong

```python
User("name"="nikita")
```

---

# Dictionary Unpacking

```python
data = {"name":"nikita","age":20}

user = User(**data)
```

`**` unpacks dictionary values.

---

# Validation

Pydantic checks types automatically.

Example:

```python
id="10"
```

Converted to:

```python
id=10
```

---

# Case Sensitivity

```python
Value != value
```

Python treats capital and small letters differently.

---

# Main Benefit

Pydantic:

* validates data
* converts types
* reduces manual checking
* creates clean backend models

```
```
````md id="b4x2gx"
# Pydantic Field() Notes

## What is Field()?

`Field()` is used in :contentReference[oaicite:0]{index=0} to add:
- validation
- constraints
- metadata
- default values

to model fields.

---

# Basic Syntax

```python
field_name: type = Field(...)
````

Example:

```python
name: str = Field(...)
```

---

# Meaning of `...`

```python
Field(...)
```

`...` means:

* field is required

Example:

```python
name: str = Field(...)
```

User must provide name.

---

# min_length

```python
min_length=3
```

Minimum number of characters.

Example:

```python
name: str = Field(min_length=3)
```

Valid:

```python
"Nikita"
```

Invalid:

```python
"ab"
```

---

# max_length

```python
max_length=30
```

Maximum number of characters allowed.

---

# description

```python
description="Employee name"
```

Adds field description.
Useful in API docs like FastAPI.

---

# example

```python
example="NikitaPandey"
```

Shows sample input.

---

# ge (Greater Than or Equal)

```python
ge=10000
```

Value must be:

* greater than
* or equal to 10000

Example:

```python
salary: int = Field(ge=10000)
```

Valid:

```python
20000
```

Invalid:

```python
5000
```

---

# le (Less Than or Equal)

```python
le=100000
```

Value must be smaller than or equal to limit.

---

# pattern

Used for regex validation.

Example:

```python
pattern=r'^\d{10}$'
```

Checks:

* exactly 10 digits

---

# Email Pattern Example

```python
email: str = Field(
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
)
```

Valid:

```python
abc@gmail.com
```

Invalid:

```python
abcgmail
```

---

# Optional Field

```python
dept: Optional[str] = "General"
```

Field can:

* contain string
* or None

Default value:

```python
"General"
```

---

# Common Field Constraints

| Constraint    | Meaning           |
| ------------- | ----------------- |
| `min_length`  | minimum text size |
| `max_length`  | maximum text size |
| `ge`          | greater/equal     |
| `le`          | less/equal        |
| `pattern`     | regex matching    |
| `description` | field explanation |
| `example`     | sample value      |

---

# Complete Example

```python
from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):

    name: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Employee Name",
        example="Nikita"
    )

    dept: Optional[str] = "General"

    salary: int = Field(
        ...,
        ge=10000,
        le=1000000
    )

    phone: str = Field(
        ...,
        pattern=r'^\d{10}$'
    )
```

---

# Main Purpose of Field()

Field() helps:

* validate data
* restrict invalid input
* document APIs
* add professional backend validation

```
```
