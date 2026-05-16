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

    
    