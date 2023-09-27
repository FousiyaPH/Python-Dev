class Employee:
    def employeeDetails(self):
        self.name = "James"
        print("Name = ",self.name)
        self.age = 30
        print("Age = ",self.age)

    def printEmployeeDetails(self):
        print("printing another method")
        print("Name: ",self.name)
        print("Age: ",self.age)

employee = Employee()
employee.employeeDetails() # Employee.employeeDetail(employee)- this statement shows how internally python makes this function call
employee.printEmployeeDetails()