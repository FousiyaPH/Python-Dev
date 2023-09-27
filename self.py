class Employee:
    def employeeDetails(self):
        self.name = "James"
        print("Name = ",self.name)
        #age is only accessible in this method
        age = 30
        print("Age = ", self.age)
    def printEmployeeDetails(self):
        print("printing another method")
        print("Name: ",self.name)
        """ 
        will get error for the below statement as NameError: name 'age' is not defined
        age attribute cannot be accessed within this method, because I haven't used the name of the object(self) to create the age attribute 
        in the employeeDetails method. so the method termintes this particular attribute cannot be used in any other methods.
        """
        print("Age: ",self.age)

employee = Employee()
employee.employeeDetails() # Employee.employeeDetail(employee)- this statement shows how internally python makes this function call
employee.printEmployeeDetails()