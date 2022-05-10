import re

def validate(password, args=None, lower=1, upper=float('inf')):
    
    valid = True
    message = "Password is acceptable"
    failed = []

    if(args==None):
        args = []

    if(lower <= 0):
        return False, "Lower limit cannot be less than 1", failed
    if(upper < lower):
        return False, "Invalid upper bound", failed

    for i, regex in enumerate(args):
        pattern = re.compile(regex)
        match = pattern.search(password)
        if(match is None):
            failed.append(i)
            valid = False
            message = "Failed regex test"

    if(len(password) < lower):
        valid = False
        message = "Password too short"

    if(len(password) > upper):
        valid = False
        message = "Password too long"

    return valid, message, failed

def main():
    print("Welcome to Password Validation Program!!")
    

if __name__ == "__main__":
    main()