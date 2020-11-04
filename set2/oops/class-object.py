class Employee:
    def __init__(self, eno, ename):
        self.eno = eno
        self.ename = ename

    def displayEmpDetails(self):
        print("Employee number : ", self.eno)
        print("Employee name : ", self.ename)


empObj = Employee(121, "Kohli")
empObj.displayEmpDetails()
