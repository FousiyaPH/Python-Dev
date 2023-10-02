class Employee:
    
    def __init__(self, name):
        self.name = name
    
    def displayEmployeeDetails(self):
        print(self.name)

# when creating the object, by default the init method will be called and initializes the attribute
employee = Employee("Mark")
employeeTwo = Employee("Zerina")
employee.displayEmployeeDetails() 
employeeTwo.displayEmployeeDetails()      