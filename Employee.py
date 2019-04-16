class Employee:
    """A sample Employee class"""

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay

    @property
    def email(self):
        return'{}.{}@email.com'.format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.firstname, self.lastname, self.pay)
