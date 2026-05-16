from functools import wraps

def logg(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("❤️we are running the log",func.__name__)
        result=func(*args,**kwargs)
        result+=1


        print("😘we are running the log",func.__name__)
        return result
    return wrapper

@logg
def chai(type):
    print(f'masala chai should be in log')
    y=2*3
    return y
    

let=chai("masala")
print(let)
    

    