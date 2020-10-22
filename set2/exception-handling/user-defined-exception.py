class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg

age=int(input("Enter Age:"))
if age>35:
    raise TooOldException("You can't apply for exam as your age is above mentioned age!!!")
elif age<16:
    raise TooYoungException("You can't apply for exam as your age is below mentioned age!!!")
else:
    print("You can apply for exam!!!")