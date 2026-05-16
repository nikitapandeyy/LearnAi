from functools import wraps

def aut(func):
    @wraps(func)
    def wrapper(userrole):
        if userrole!="admin":
            print("sorry authenitication is not granted")
            return None #this is explicitly need cause this python req to have return value but not in updated python anymore
        else:
            return func(userrole)
    return wrapper

@aut
def log(user):
    print("access granted")
log("user")
log("admin")