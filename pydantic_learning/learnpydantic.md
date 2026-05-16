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
````md id="m9x4qp"
# Pydantic Validators Notes

## What are Validators?

Validators in :contentReference[oaicite:0]{index=0} are used to:
- check data
- apply custom rules
- raise errors if data is invalid

They run automatically when object is created.

---

# Types of Validators

| Validator | Purpose |
|---|---|
| `@field_validator` | validates single field |
| `@model_validator` | validates entire model |

---

# Field Validator

## Your Code

```python
from pydantic import BaseModel, field_validator

class Username(BaseModel):

    username: str

    @field_validator('username')
    def username_len(cls, v):

        if len(v) < 4:
            raise ValueError("password greater than 4")

        return v
````

---

# Flow of Execution

## Step 1

User creates object:

```python id="88gqvk"
u = Username(username="nik")
```

---

# Step 2

Pydantic checks:

* field types
* validators

---

# Step 3

Validator runs automatically:

```python id="w2hxvv"
username_len(cls, v)
```

Here:

```python id="25rqwl"
v = "nik"
```

---

# Step 4

Condition:

```python id="q31onl"
if len(v) < 4:
```

becomes:

```python id="8t7r83"
True
```

---

# Step 5

Error raised:

```python id="up9zbb"
raise ValueError("password greater than 4")
```

Pydantic stops object creation.

---

# If Valid

```python id="x7lxq0"
u = Username(username="nikita")
```

Validator returns:

```python id="7mqvyl"
return v
```

Object successfully created.

---

# Important Parts

| Part               | Meaning           |
| ------------------ | ----------------- |
| `cls`              | class itself      |
| `v`                | field value       |
| `return v`         | validated value   |
| `raise ValueError` | validation failed |

---

# model_validator

Used for:

* checking multiple fields together
* cross-field validation

---

# Your Code

```python
from pydantic import BaseModel, model_validator

class Passwd(BaseModel):

    curr_pswd: str
    knw_passwd: str

    @model_validator(mode='after')
    def psswrd_Check(cls, values):

        if values.curr_pswd != values.knw_passwd:
            raise ValueError("password mismatched")

        return values
```

---

# Flow of Execution

---

# Step 1

Object creation:

```python id="0hkr4r"
p = Passwd(
    curr_pswd="abc123",
    knw_passwd="xyz"
)
```

---

# Step 2

Pydantic validates:

* field types first

---

# Step 3

After fields validated:

```python id="3ltl8v"
@model_validator(mode='after')
```

runs.

---

# Step 4

Condition checked:

```python id="0h0t7s"
values.curr_pswd != values.knw_passwd
```

---

# Step 5

If different:

```python id="0m89ui"
raise ValueError("password mismatched")
```

Error occurs.

---

# If Same

```python id="gq6y3l"
curr_pswd="abc123"
knw_passwd="abc123"
```

Then:

```python id="nhyixv"
return values
```

Object created successfully.

---

# What is mode='after' ?

Means:

* run validator after all fields are validated

Other mode:

```python id="hn14gc"
mode='before'
```

runs before validation.

---

# Difference Between Validators

| Validator         | Checks       |
| ----------------- | ------------ |
| `field_validator` | one field    |
| `model_validator` | entire model |

---

# Common Uses

## field_validator

* username length
* email format
* phone number rules

---

# model_validator

* password confirmation
* comparing fields
* business logic checks

---

# Validation Flow in Pydantic

```text id="2t1zwg"
Input Data
    ↓
Type Validation
    ↓
Field Validators
    ↓
Model Validators
    ↓
Object Created
```

---

# Important Learning

Validators help:

* enforce custom rules
* prevent invalid data
* secure backend systems
* add business logic validation

```
```
````md id="y7f2kp"
# Pydantic computed_field Notes

## What is computed_field?

`@computed_field` in :contentReference[oaicite:0]{index=0} is used to:
- create calculated fields
- generate values dynamically
- include calculated values in `model_dump()`

without storing them manually.

---

# Your Code

```python
from pydantic import BaseModel, computed_field

class Hotel_mng(BaseModel):

    name: str
    night: int
    price: int
    room_id: int
    user_id: int

    @computed_field
    @property
    def calculateprice(self) -> float:

        return self.night * self.price


user = Hotel_mng(
    name="nikita",
    night=3,
    price=10000,
    room_id=567,
    user_id=7887
)

print(user.calculateprice)
print(user.model_dump())
````

---

# Output

```python id="8q8pxq"
30000
```

```python id="v5ol9r"
{
 'name': 'nikita',
 'night': 3,
 'price': 10000,
 'room_id': 567,
 'user_id': 7887,
 'calculateprice': 30000
}
```

---

# Main Concept

You are creating:

* a normal model
* plus a calculated field

where:

```python id="65e6pj"
total price = nights × room price
```

---

# Step-by-Step Flow

---

# Step 1 → Model Creation

Python creates model:

```python id="9x9jlwm"
class Hotel_mng(BaseModel):
```

with fields:

* name
* night
* price
* room_id
* user_id

---

# Step 2 → computed_field Defined

```python id="mwwn7w"
@computed_field
@property
def calculateprice(self):
```

This creates:

* calculated property
* not manually stored
* generated dynamically

---

# Step 3 → Object Creation

```python id="g5pd1j"
user = Hotel_mng(...)
```

Object stores:

```python id="jyfqvn"
night = 3
price = 10000
```

---

# Step 4 → Accessing calculateprice

```python id="i7c3em"
print(user.calculateprice)
```

Python runs:

```python id="l5uq9l"
return self.night * self.price
```

Equivalent to:

```python id="jlwm12"
3 * 10000
```

Result:

```python id="jlwm98"
30000
```

---

# Why @property Used?

Without:

```python id="9z7mxn"
@property
```

you would need:

```python id="jlwm11"
user.calculateprice()
```

with parentheses.

But with `@property`:

```python id="jlwm44"
user.calculateprice
```

works like normal attribute.

---

# Why @computed_field Used?

Normally properties are NOT included in:

```python id="jlwm77"
model_dump()
```

But:

```python id="jlwm33"
@computed_field
```

tells Pydantic:

> "Include this calculated property in serialization/output."

---

# model_dump()

```python id="jlwm90"
print(user.model_dump())
```

converts model into dictionary.

Equivalent to:

```python id="jlwm08"
{
  "name": "nikita",
  ...
}
```

---

# Important Understanding

`calculateprice` is:

* NOT stored in database/model
* calculated every time dynamically

---

# Real Life Analogy

Hotel stores:

* nights
* room price

but:

```python id="jlwm55"
total_price
```

is calculated automatically.

---

# Visual Flow

```text id="jlwm73"
night = 3
price = 10000
        ↓
calculateprice
        ↓
3 × 10000
        ↓
30000
```

---

# Difference Between Normal Field and Computed Field

| Normal Field        | Computed Field          |
| ------------------- | ----------------------- |
| stored directly     | calculated dynamically  |
| user provides value | generated automatically |
| static              | dynamic                 |

---

# Important Concepts Learned

| Concept           | Meaning                     |
| ----------------- | --------------------------- |
| `@property`       | use method like attribute   |
| `@computed_field` | include calculated field    |
| `self`            | current object              |
| `model_dump()`    | convert model to dictionary |

---

# Main Benefit

Computed fields help:

* avoid duplicate data
* calculate values dynamically
* create cleaner models
* generate derived values automatically

---

# Real Use Cases

* total hotel bill
* GST calculation
* total cart amount
* age from birth year
* discounted price
* salary after tax

```
```
````md id="h2x8qp"
# Pydantic Validators Notes

## Validators in Pydantic

Validators are functions used to:
- validate data
- clean data
- transform data
- apply custom rules

They run automatically during object creation.

---

# Types of Validators

| Validator | Purpose |
|---|---|
| `@field_validator` | validates single field |
| `@model_validator` | validates entire model |

---

# field_validator

Used for:
- checking one field
- modifying one field

---

# Syntax

```python
@field_validator('field_name')
def validate(cls, v):
    return v
````

---

# Important Parameters

| Parameter | Meaning             |
| --------- | ------------------- |
| `cls`     | class itself        |
| `v`       | current field value |

---

# Example 1 → Name Validation

```python
class Person(BaseModel):

    f_name: str
    l_name: str

    @field_validator('f_name', 'l_name')
    def nums_cap(cls, v):

        if not v.istitle():
            raise ValueError("name must be capitalized")

        return v
```

---

# What Happens?

Checks:

* first name
* last name

must start with capital letters.

---

# Example

## Valid

```python
"Nikita"
```

## Invalid

```python
"nikita"
```

---

# istitle()

```python
v.istitle()
```

Checks whether:

* first letter is uppercase

Example:

```python
"Nikita" → True
"nikita" → False
```

---

# Important Fix

## Wrong

```python
@field_validator(f_name,l_name)
```

## Correct

```python
@field_validator('f_name', 'l_name')
```

Field names must be strings.

---

# Example 2 → Email Normalization

```python
class user(BaseModel):

    email: str

    @field_validator('email')
    def normalize(cls, v):

        return v.lower().strip()
```

---

# What Happens?

Input:

```python
"   Nikita@GMAIL.COM "
```

Converted into:

```python
"nikita@gmail.com"
```

---

# lower()

```python
v.lower()
```

Converts text into lowercase.

---

# strip()

```python
v.strip()
```

Removes extra spaces.

---

# Example 3 → Price Parsing

```python
class Product(BaseModel):

    price: str

    @field_validator('price')
    def parse(cls, v):

        if isinstance(v, str):

            return float(
                v.replace('$', '').replace(',', '')
            )

        return v
```

---

# What Happens?

Input:

```python
"$10,000"
```

Converted into:

```python
10000.0
```

---

# replace()

```python
replace('$', '')
```

Removes dollar sign.

---

# isinstance()

```python
isinstance(v, str)
```

Checks whether value is string.

---

# model_validator

Used for:

* checking multiple fields together
* cross-field validation

---

# Syntax

```python
@model_validator(mode='after')
def validate(cls, values):
    return values
```

---

# Example 4 → Date Validation

```python
class check_time(BaseModel):

    s_date: datetime
    e_date: datetime

    @model_validator(mode='after')
    def check(cls, v):

        if v.s_date >= v.e_date:
            raise ValueError("sorry cant be right")

        return v
```

---

# What Happens?

Checks:

* start date must be before end date

---

# Example

## Valid

```python
s_date = Jan 1
e_date = Jan 5
```

## Invalid

```python
s_date = Jan 10
e_date = Jan 5
```

---

# Important Fix

## Wrong

```python
v.end_date
```

## Correct

```python
v.e_date
```

because field name is `e_date`.

---

# mode='after'

Means:

* validator runs after field validation

Flow:

```text
Input Data
    ↓
Field Validation
    ↓
Model Validation
    ↓
Object Created
```

---

# Why return v ?

Validators must return:

* validated value
* transformed value

---

# Example

```python
return v.lower().strip()
```

returns cleaned email.

Without return:

* Python returns None
* Pydantic stores None

---

# Validation Flow

```text
Input Value
    ↓
Validator Runs
    ↓
Check / Transform
    ↓
return v
    ↓
Final Value Stored
```

---

# Common Uses of Validators

## field_validator

* username checks
* email cleaning
* phone validation
* price conversion

---

# model_validator

* password matching
* date checking
* business logic validation

---

# Important Concepts Learned

| Concept            | Meaning                   |
| ------------------ | ------------------------- |
| `field_validator`  | validates single field    |
| `model_validator`  | validates full model      |
| `return v`         | final validated value     |
| `raise ValueError` | validation failed         |
| `strip()`          | removes spaces            |
| `lower()`          | lowercase conversion      |
| `replace()`        | replace/remove characters |
| `isinstance()`     | type checking             |

---

# Main Benefit

Validators help:

* clean data
* secure input
* prevent invalid values
* apply custom business rules

```
```

````md id="p8w2mz"
# Nested Models & Automatic Conversion Notes

## Your Code

```python
from pydantic import BaseModel
from typing import List, Optional


class Adress(BaseModel):

    street: str
    pst: str
    state: str


class User(BaseModel):

    name: str
    phone: int
    adr: Adress


adrs = Adress(
    street="value1",
    pst="7887",
    state="up"
)

user = User(
    name="nikita",
    phone=788778,
    adr=adrs
)

user_data = {
    'name': 'nikita',
    'phone': '45343',
    'adr': {
        'street': 'effe',
        'pst': 'frwf',
        'state': "hu"
    }
}

print(user)

lan = User(**user_data)

print(lan)
````

---

# Output Understanding

## First Output

```python
name='nikita'
phone=788778
adr=Adress(street='value1', pst='7887', state='up')
```

This comes from:

```python
user = User(..., adr=adrs)
```

where:

* `adrs` is already an Address model object.

---

# Second Output

```python
name='nikita'
phone=45343
adr=Adress(street='effe', pst='frwf', state='hu')
```

This comes from:

```python
lan = User(**user_data)
```

---

# Main Concept Learned

Pydantic automatically:

* converts dictionaries into nested models
* converts data types automatically

---

# Step-by-Step Flow

---

# Step 1 → Dictionary Input

```python
user_data = {
    ...
}
```

contains:

* phone as string
* adr as dictionary

---

# Step 2 → Dictionary Unpacking

```python
User(**user_data)
```

Equivalent to:

```python
User(
    name='nikita',
    phone='45343',
    adr={
        ...
    }
)
```

`**` unpacks dictionary into keyword arguments.

---

# Step 3 → Type Validation

Pydantic sees:

```python
phone: int
```

but input is:

```python
'45343'
```

string.

Pydantic automatically converts:

```python
'45343' → 45343
```

---

# Step 4 → Nested Model Conversion

Pydantic sees:

```python
adr: Adress
```

but input is dictionary:

```python
{
   'street':'effe',
   ...
}
```

Pydantic automatically creates:

```python
Adress(
    street='effe',
    pst='frwf',
    state='hu'
)
```

---

# Visual Flow

```text
Dictionary Input
       ↓
User(**user_data)
       ↓
Pydantic Validation
       ↓
String → Integer conversion
       ↓
Dictionary → Adress Model conversion
       ↓
Final User Object
```

---

# Important Understanding

You did NOT manually create:

```python
Adress(...)
```

for second user.

Pydantic created it automatically.

---

# Nested Model Concept

```python
adr: Adress
```

means:

> adr field must contain Address-type data.

Pydantic accepts:

* Address object
  OR
* dictionary

and converts automatically.

---

# Automatic Type Conversion

## Input

```python
phone='45343'
```

## Converted Into

```python
phone=45343
```

because field type is:

```python
phone: int
```

---

# Why Pydantic Powerful?

Pydantic automatically:

* validates
* converts
* structures data

with minimal code.

---

# Real World Use

This is heavily used in:

* FastAPI
* APIs
* JSON parsing
* backend systems
* database schemas

---

# JSON Structure Understanding

Your nested data looks like:

```python
{
    "name": "nikita",
    "phone": "45343",
    "adr": {
        "street": "effe",
        "pst": "frwf",
        "state": "hu"
    }
}
```

Very similar to API request body.

---

# Important Concepts Learned

| Concept              | Meaning                     |
| -------------------- | --------------------------- |
| nested model         | model inside another model  |
| `**data`             | dictionary unpacking        |
| automatic conversion | type conversion by Pydantic |
| dictionary → model   | automatic nested parsing    |
| validation           | checking input types        |

---

# Main Learning

Pydantic can:

* parse nested dictionaries
* create nested objects automatically
* convert types automatically
* validate structured data cleanly

```
```
````md id="n4m8zp"
# Self Referencing Models in Pydantic

## What is Self Referencing?

Self referencing means:
- a model contains itself
- model refers to same model type inside it

---

# Real Life Example

Comments in social media:

```text
Comment
   └── Replies
          └── Replies to replies
                 └── More replies
````

Each reply is also a Comment.

So:

* Comment contains List of Comment

This is called:

* recursive model
* self referencing model

---

# Your Code

```python
from pydantic import BaseModel
from typing import List, Optional


class Comment(BaseModel):

    id: int
    content: str

    reply: Optional[List["Comment"]] = None


Comment.model_rebuild()


comment = Comment(
    id=1,
    content="this is hillarious",

    reply=[

        Comment(
            id=2,
            content="wow u must be amazing "
        ),

        Comment(
            id=2,
            content="no u are "
        ),

        Comment(
            id=2,
            content="bye",
            reply=[]
        )
    ]
)

print(comment)
```

---

# Main Concept

```python
reply: Optional[List["Comment"]]
```

means:

> reply field contains list of Comment objects.

Comment is referring to itself.

---

# Why "Comment" in Quotes?

```python
"Comment"
```

is called:

* Forward Reference

Because:

* class is still being created
* Python has not fully defined Comment yet

So we use string:

```python
"Comment"
```

instead of:

```python
Comment
```

---

# What Does This Mean?

```python
Optional[List["Comment"]]
```

Breakdown:

| Part        | Meaning         |
| ----------- | --------------- |
| `List`      | multiple items  |
| `"Comment"` | Comment objects |
| `Optional`  | can be None     |

---

# Meaning Together

```python
reply: Optional[List["Comment"]]
```

means:

> replies can contain multiple Comment objects or None.

---

# Why model_rebuild() Needed?

```python
Comment.model_rebuild()
```

tells Pydantic:

> "Now resolve the forward references."

Because:

* `"Comment"` was string initially
* Pydantic now converts it into actual model reference

---

# Without model_rebuild()

Pydantic may not understand:

* recursive references
* forward referenced types

especially in complex nested models.

---

# Flow of Execution

---

# Step 1 → Class Creation

Python creates:

```python
class Comment(BaseModel):
```

---

# Step 2 → Forward Reference Stored

Pydantic sees:

```python
"Comment"
```

as temporary string reference.

---

# Step 3 → model_rebuild()

```python
Comment.model_rebuild()
```

Pydantic resolves:

* string reference
* into actual Comment model

---

# Step 4 → Main Comment Created

```python
comment = Comment(...)
```

Main parent comment created.

---

# Step 5 → Replies Created

Inside:

```python
reply=[
   Comment(...),
   Comment(...),
]
```

each reply becomes:

* another Comment object

---

# Visual Structure

```text
Comment(id=1)
│
├── Reply 1
│      └── Comment(id=2)
│
├── Reply 2
│      └── Comment(id=2)
│
└── Reply 3
       └── Comment(id=2)
```

---

# Nested Recursive Structure

This structure can continue infinitely:

```text
Comment
   └── Reply
          └── Reply
                 └── Reply
```

---

# Output Understanding

```python
print(comment)
```

prints nested model structure.

Pydantic recursively prints:

* parent comment
* child replies

---

# Why Optional Used?

```python
Optional[List["Comment"]]
```

means:

* replies may exist
  OR
* can be None

Example:

```python
reply=None
```

or:

```python
reply=[]
```

---

# Difference Between None and Empty List

| Value  | Meaning                        |
| ------ | ------------------------------ |
| `None` | no replies field               |
| `[]`   | replies field exists but empty |

---

# Real World Use Cases

Self referencing models are used in:

* comment systems
* social media threads
* file systems
* organization hierarchy
* tree structures
* category/subcategory systems

---

# Tree Structure Understanding

Your model behaves like:

```text
Tree
 ├── Parent
 │     ├── Child
 │     ├── Child
 │     └── Child
```

This is recursive data structure.

---

# Important Concepts Learned

| Concept           | Meaning                     |
| ----------------- | --------------------------- |
| self referencing  | model refers to itself      |
| recursive model   | nested repeating model      |
| forward reference | using model name as string  |
| `model_rebuild()` | resolves forward references |
| nested structure  | model inside same model     |

---

# Main Learning

Pydantic allows:

* recursive models
* deeply nested structures
* tree-like data modeling
* automatic nested validation

using self referencing models.

```
```

````md id="x7n4qp"
# Pydantic Serialization Notes

# What is Serialization?

Serialization means:

> Converting Python objects into transferable/storable formats.

Usually into:
- Dictionary
- JSON
- API response
- Database format

---

# Why Serialization Needed?

Python objects cannot directly:
- travel through APIs
- be stored in JSON
- be sent over network

So we convert them into:
- JSON
- dictionaries
- strings

---

# Real Life Example

```text
Python Object
      ↓
Serialization
      ↓
JSON / Dictionary
      ↓
Send to API / Frontend / Database
````

---

# Your Code

```python
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Adress(BaseModel):

    street: str
    post: str


class User(BaseModel):

    name: str
    email: str
    is_active: bool

    adrs: Adress

    createdAt: datetime

    model_config = ConfigDict(

        json_encoders={

            datetime: lambda v:
            v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


user = User(

    name="nikita",
    email="jbhyg",
    is_active=True,

    adrs=Adress(
        street="hg",
        post="jhb"
    ),

    createdAt=datetime(32,4,3,2,13,2)
)

print(user)

print(user.model_dump())

print(user.model_dump_json())
```

---

# Main Concepts Learned

This code teaches:

* serialization
* JSON conversion
* nested serialization
* custom encoders
* datetime formatting

---

# Step-by-Step Flow

---

# Step 1 → Object Creation

```python
user = User(...)
```

creates Pydantic model object.

Object contains:

* strings
* booleans
* nested model
* datetime object

---

# Step 2 → Printing Object

```python
print(user)
```

Output:

```python
name='nikita'
email='jbhyg'
...
```

This is:

* raw Pydantic representation

NOT serialization yet.

---

# Step 3 → model_dump()

```python
user.model_dump()
```

Converts model into:

* Python dictionary

---

# Output

```python
{
 'name': 'nikita',
 'email': 'jbhyg',
 'is_active': True,
 'adrs': {
      'street': 'hg',
      'post': 'jhb'
 },
 'createdAt': datetime.datetime(...)
}
```

---

# Important Understanding

`model_dump()` gives:

* Python-native dictionary
* datetime remains datetime object

NOT JSON string.

---

# Step 4 → model_dump_json()

```python
user.model_dump_json()
```

Converts model into:

* JSON string

---

# Output

```json
{
  "name":"nikita",
  "email":"jbhyg",
  "is_active":true,
  ...
}
```

Now:

* booleans become JSON booleans
* datetime becomes string

---

# Difference Between model_dump and model_dump_json

| Method              | Output            |
| ------------------- | ----------------- |
| `model_dump()`      | Python dictionary |
| `model_dump_json()` | JSON string       |

---

# Nested Serialization

Your model contains:

```python
adrs: Adress
```

Nested model automatically becomes:

```python
{
   "street":"hg",
   "post":"jhb"
}
```

during serialization.

---

# What is ConfigDict?

```python
model_config = ConfigDict(...)
```

Used to configure model behavior.

In Pydantic V2:

* replaces old Config class

---

# json_encoders

```python
json_encoders = {
    datetime: lambda v: ...
}
```

Used for:

* custom serialization logic

---

# Why Needed?

Python datetime object:

```python
datetime.datetime(...)
```

cannot always serialize cleanly into JSON.

So we define:

* how datetime should convert into string

---

# lambda Function

```python
lambda v: ...
```

means:

* small anonymous function

Equivalent to:

```python
def convert(v):
    return ...
```

---

# strftime()

```python
v.strftime('%d-%m-%Y %H:%M:%S')
```

Formats datetime into custom string.

---

# Format Meaning

| Symbol | Meaning |
| ------ | ------- |
| `%d`   | day     |
| `%m`   | month   |
| `%Y`   | year    |
| `%H`   | hour    |
| `%M`   | minute  |
| `%S`   | seconds |

---

# Your Small Mistake

You wrote:

```python
'%d-%m-%Y %H:%M:$S'
```

Wrong:

```python
$S
```

Correct:

```python
%S
```

---

# Correct Formatter

```python
v.strftime('%d-%m-%Y %H:%M:%S')
```

---

# Serialization Flow

```text
Pydantic Model
      ↓
model_dump()
      ↓
Python Dictionary
```

---

```text
Pydantic Model
      ↓
model_dump_json()
      ↓
JSON String
```

---

# JSON vs Python Dictionary

| Python Dict     | JSON     |
| --------------- | -------- |
| `True`          | `true`   |
| `'text'`        | `"text"` |
| datetime object | string   |

---

# Why Serialization Important?

Serialization is heavily used in:

* FastAPI
* REST APIs
* databases
* frontend-backend communication
* caching
* microservices

---

# Real World API Example

Backend sends:

```json
{
   "name":"nikita",
   "createdAt":"03-04-0032 02:13:02"
}
```

Frontend receives clean JSON.

---

# Advanced Understanding

Pydantic serialization:

* recursively serializes nested models
* converts special types
* applies custom encoders
* produces API-ready output

---

# Important Concepts Learned

| Concept              | Meaning                      |
| -------------------- | ---------------------------- |
| serialization        | object → transferable format |
| `model_dump()`       | convert to dict              |
| `model_dump_json()`  | convert to JSON              |
| `ConfigDict`         | model configuration          |
| `json_encoders`      | custom serialization         |
| `strftime()`         | datetime formatting          |
| nested serialization | serialize nested models      |

---

# Main Learning

Pydantic serialization helps:

* convert models into API-ready JSON
* customize output formatting
* serialize nested objects automatically
* control how complex types are represented

```
```
