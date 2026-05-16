````md id="a7m2wd"
# Python Decorators Notes

## What is a Decorator?

A decorator is a function that:
- takes another function
- adds extra functionality
- returns modified function

without changing original function code.

---

# Basic Structure

```python
def decorator(func):

    def wrapper():
        # extra work
        func()

    return wrapper
````

---

# Your Example

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper():
        print("hello i am using this")

        func()

        print("after i am using this")

    return wrapper


@decorator
def greet():
    print("namaste india")


greet()

print(greet.__name__)
```

---

# Output

```python
hello i am using this
namaste india
after i am using this
greet
```

---

# Flow of Execution

## Step 1

```python
@decorator
```

means:

```python
greet = decorator(greet)
```

Decorator replaces original function with wrapper.

---

# Step 2

When:

```python
greet()
```

is called:

Actually:

```python
wrapper()
```

runs.

---

# Step 3

Inside wrapper:

```python
print("hello i am using this")
```

Runs before original function.

---

# Step 4

```python
func()
```

calls original function:

```python
greet()
```

which prints:

```python
namaste india
```

---

# Step 5

After original function:

```python
print("after i am using this")
```

runs.

---

# What is wrapper()?

`wrapper()` is:

* inner function
* used to add extra behavior

before or after original function.

---

# Why Use Decorators?

Decorators are used for:

* logging
* authentication
* timing functions
* caching
* validation
* debugging

without modifying original code.

---

# Problem Without wraps

Without:

```python
@wraps(func)
```

this happens:

```python
print(greet.__name__)
```

Output:

```python
wrapper
```

because decorator replaces original function metadata.

---

# Purpose of wraps

```python
from functools import wraps
```

`wraps()` preserves:

* original function name
* docstring
* metadata

---

# With wraps

Output:

```python
greet
```

instead of:

```python
wrapper
```

---

# Common Errors You Faced

## 1. Missing @wraps

Wrong:

```python
wraps(func)
```

Correct:

```python
@wraps(func)
```

Decorator syntax needs `@`.

---

# 2. Indentation Error

Wrong indentation caused:

```python
SyntaxError
```

Python is indentation-sensitive.

---

# 3. Calling Function Outside Wrapper

You accidentally called:

```python
func()
```

outside wrapper.

That executed function immediately.

---

# Simple Analogy

Decorator is like:

> "Gift wrapping around a function."

Original function stays same,
but extra behavior is added around it.

---

# Important Concepts Learned

| Concept    | Meaning                    |
| ---------- | -------------------------- |
| decorator  | modifies function behavior |
| wrapper    | inner function             |
| @decorator | applies decorator          |
| @wraps     | preserves metadata         |
| func()     | calls original function    |

---

# Short Syntax Understanding

```python
@decorator
def greet():
```

Equivalent to:

```python
greet = decorator(greet)
```

---

# Real World Use Cases

* Flask routes
* FastAPI APIs
* Authentication systems
* Timing execution
* Logging systems
* Retry mechanisms

```
```

````md id="a7m2wd"
# Python Decorators Notes

## What is a Decorator?

A decorator is a function that:
- takes another function
- adds extra functionality
- returns modified function

without changing original function code.

---

# Basic Structure

```python
def decorator(func):

    def wrapper():
        # extra work
        func()

    return wrapper
````

---

# Your Example

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper():
        print("hello i am using this")

        func()

        print("after i am using this")

    return wrapper


@decorator
def greet():
    print("namaste india")


greet()

print(greet.__name__)
```

---

# Output

```python
hello i am using this
namaste india
after i am using this
greet
```

---

# Flow of Execution

## Step 1

```python
@decorator
```

means:

```python
greet = decorator(greet)
```

Decorator replaces original function with wrapper.

---

# Step 2

When:

```python
greet()
```

is called:

Actually:

```python
wrapper()
```

runs.

---

# Step 3

Inside wrapper:

```python
print("hello i am using this")
```

Runs before original function.

---

# Step 4

```python
func()
```

calls original function:

```python
greet()
```

which prints:

```python
namaste india
```

---

# Step 5

After original function:

```python
print("after i am using this")
```

runs.

---

# What is wrapper()?

`wrapper()` is:

* inner function
* used to add extra behavior

before or after original function.

---

# Why Use Decorators?

Decorators are used for:

* logging
* authentication
* timing functions
* caching
* validation
* debugging

without modifying original code.

---

# Problem Without wraps

Without:

```python
@wraps(func)
```

this happens:

```python
print(greet.__name__)
```

Output:

```python
wrapper
```

because decorator replaces original function metadata.

---

# Purpose of wraps

```python
from functools import wraps
```

`wraps()` preserves:

* original function name
* docstring
* metadata

---

# With wraps

Output:

```python
greet
```

instead of:

```python
wrapper
```

---

# Common Errors You Faced

## 1. Missing @wraps

Wrong:

```python
wraps(func)
```

Correct:

```python
@wraps(func)
```

Decorator syntax needs `@`.

---

# 2. Indentation Error

Wrong indentation caused:

```python
SyntaxError
```

Python is indentation-sensitive.

---

# 3. Calling Function Outside Wrapper

You accidentally called:

```python
func()
```

outside wrapper.

That executed function immediately.

---

# Simple Analogy

Decorator is like:

> "Gift wrapping around a function."

Original function stays same,
but extra behavior is added around it.

---

# Important Concepts Learned

| Concept    | Meaning                    |
| ---------- | -------------------------- |
| decorator  | modifies function behavior |
| wrapper    | inner function             |
| @decorator | applies decorator          |
| @wraps     | preserves metadata         |
| func()     | calls original function    |

---

# Short Syntax Understanding

```python
@decorator
def greet():
```

Equivalent to:

```python
greet = decorator(greet)
```

---

# Real World Use Cases

* Flask routes
* FastAPI APIs
* Authentication systems
* Timing execution
* Logging systems
* Retry mechanisms

```
```
No. You do **not** need to keep the exact same arguments in `wrapper()` as the original function, but the wrapper must be able to accept whatever arguments are passed to the original function.

That is why decorators usually use:

```python
def wrapper(*args, **kwargs):
```

This makes the wrapper flexible.

---

# Your Example

Original function:

```python
def chai(type):
```

takes:

* one positional argument

But wrapper:

```python
def wrapper(*args, **kwargs):
```

can accept:

* any number of positional arguments
* any keyword arguments

So when:

```python
chai("masala")
```

runs:

```python
args = ("masala",)
```

Then:

```python
func(*args, **kwargs)
```

becomes:

```python
func("masala")
```

which correctly calls original `chai()`.

---

# Why We Use *args and **kwargs

Because decorator should work for many functions.

Example:

```python
@logg
def add(a, b):
    return a + b


@logg
def greet(name, age):
    print(name, age)
```

Same decorator works for both because wrapper accepts everything.

---

# Without *args and **kwargs

If wrapper is:

```python
def wrapper():
```

Then this fails:

```python
chai("masala")
```

Error:

```python
TypeError
```

because wrapper cannot accept arguments.

---

# Can Wrapper Have Same Arguments?

Yes.

Example:

```python
def wrapper(type):
```

works for this specific function.

But then decorator only works for functions having same parameters.

Not reusable.

---

# Best Practice

Use:

```python
def wrapper(*args, **kwargs):
```

because:

* generic
* reusable
* works for any function

---

# Flow Understanding

```text
chai("masala")
      ↓
wrapper("masala")
      ↓
args = ("masala",)
      ↓
func(*args)
      ↓
original chai("masala")
```

---

# Quick Notes

| Syntax                  | Meaning              |
| ----------------------- | -------------------- |
| `*args`                 | positional arguments |
| `**kwargs`              | keyword arguments    |
| `func(*args, **kwargs)` | forwards arguments   |
| flexible wrapper        | reusable decorator   |



````md id="4n1k5p"
# Authentication Decorator Notes

## Your Code

```python
from functools import wraps

def aut(func):

    @wraps(func)
    def wrapper(userrole):

        if userrole != "admin":

            print("sorry authentication is not granted")
            return None

        else:
            return func(userrole)

    return wrapper


@aut
def log(user):
    print("access granted")


log("user")
log("admin")
````

---

# Output

```python
sorry authentication is not granted
access granted
```

---

# Main Concept

This decorator is performing:

* authentication
* access control

before allowing function execution.

---

# Step-by-Step Flow

---

# Step 1 → Function Creation

Python creates:

```python id="1jq3pj"
def log(user):
```

---

# Step 2 → Decorator Applied

Python sees:

```python id="7v3t4m"
@aut
```

Equivalent to:

```python id="54dhho"
log = aut(log)
```

Now:

* original `log()` is passed into `aut(func)`

Here:

```python id="a7n1h7"
func = log
```

---

# Step 3 → wrapper Returned

Inside:

```python id="wjlwmh"
def aut(func):
```

Python creates:

```python id="owrvf1"
def wrapper(userrole):
```

and returns it.

Now:

```python id="v8eh7y"
log = wrapper
```

Original function is replaced by wrapper.

---

# Step 4 → Calling log("user")

You write:

```python id="jlwm4g"
log("user")
```

Actually runs:

```python id="jlwmw1"
wrapper("user")
```

---

# Step 5 → Condition Check

Inside wrapper:

```python id="s0jlwm"
if userrole != "admin":
```

"user" is not admin.

Condition becomes:

```python id="jlwm5d"
True
```

---

# Step 6 → Access Denied

```python id="jlwm0j"
print("sorry authentication is not granted")
```

Output:

```python id="jlwmg6"
sorry authentication is not granted
```

Then:

```python id="jlwm4s"
return None
```

stops execution.

Original `log()` function never runs.

---

# Step 7 → Calling log("admin")

You write:

```python id="jlwmj2"
log("admin")
```

Actually:

```python id="jlwmhf"
wrapper("admin")
```

runs.

---

# Step 8 → Condition Fails

```python id="jlwmg8"
if userrole != "admin":
```

becomes:

```python id="jlwm7t"
False
```

So Python goes to:

```python id="jlwm1x"
else:
```

---

# Step 9 → Original Function Executes

```python id="jlwm0f"
return func(userrole)
```

Equivalent to:

```python id="jlwm9v"
log("admin")
```

Original function runs:

```python id="jlwmhf"
print("access granted")
```

Output:

```python id="jlwmwv"
access granted
```

---

# Visual Flow

```text id="jlwm8v"
log("user")
      ↓
wrapper("user")
      ↓
check role
      ↓
NOT admin
      ↓
access denied
```

---

```text id="jlwmv4"
log("admin")
      ↓
wrapper("admin")
      ↓
check role
      ↓
admin verified
      ↓
original log()
      ↓
access granted
```

---

# Purpose of return None

```python id="jlwmhf"
return None
```

Means:

* stop function execution
* return empty value

Without it:

* function still exits
* because Python automatically returns `None`

So this works too:

```python id="jlwm44"
if userrole != "admin":
    print("Access denied")
    return
```

or even:

```python id="jlwm9p"
if userrole != "admin":
    print("Access denied")
```

because Python automatically returns `None`.

---

# Important Understanding

Decorator is controlling:

* who can access function
* before original function runs

This is how:

* login systems
* admin panels
* APIs
* web frameworks

handle authentication.

---

# Why wraps() Used

```python id="jlwm4r"
@wraps(func)
```

preserves:

* original function name
* metadata
* docstring

Without wraps:

```python id="jlwm3e"
log.__name__
```

would become:

```python id="jlwmk9"
wrapper
```

With wraps:

```python id="jlwm2n"
log
```

---

# Important Concepts Learned

| Concept        | Meaning                |
| -------------- | ---------------------- |
| decorator      | modifies behavior      |
| authentication | access checking        |
| wrapper        | controls execution     |
| return None    | stops execution        |
| func(userrole) | original function call |
| @wraps         | preserves metadata     |

---

# Main Learning

Decorator can:

* block execution
* allow execution
* validate users
* control permissions

before original function runs.

```
```
