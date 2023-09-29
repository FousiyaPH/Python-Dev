class Employee:
    def employeeDetails(self):
        self.name = "Ben"
#shows error (TypeError: Employee.welcomeMessage() takes 0 positional arguments but 1 was given)
# if we haven't passed the self parameter in the below function. 
# We can use static methods that do not take the self parameter
    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization")
employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()