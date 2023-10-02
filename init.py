class Employee:
    def enterEmployeeDetails(self):
        self.name = "Mark"
    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee()
# when calling the below function we will ger error like AttributeError: 'Employee' object has no attribute 'name'
# because the name attribute not initialized. the name attribute initialized only  when calling this method - 
# lette employee.enterEmployeeDetails()
employee.displayEmployeeDetails()       