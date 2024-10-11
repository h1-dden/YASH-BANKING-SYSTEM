from view import login

def login_status_check(bank_transaction):

    def wrapper_function(*args,**kwargs):

        if not login.login_status:
            raise Exception("Login is required to access this functionality")
        
        return bank_transaction(*args,**kwargs)
    
    return wrapper_function