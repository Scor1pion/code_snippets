
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

#note the follow 2 statements are the same, emp_1 is the instant variable that is passed to self
emp_1.fullname()
Employee.fullname(emp_1)

#the self is always the instance variable
    def fullname():
        return '{} {}'.format(self.first, self.last)
 print(emp_fullname())
#warning
