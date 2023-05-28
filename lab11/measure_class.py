class measure:

    def __init__(self, feet = 0, inches = 0):

        if inches > 12:

            added = inches//12

            subtract = added * 12

            self.feet = feet + added

            self.inches = inches - subtract

        else:

            self.feet = feet

            self.inches = inches

    def __str__(self):

        return "{}' {}{} ".format(self.feet, self.inches, '"')

    def __add__(self, other):

        feet = self.feet + other.feet

        inches = self.inches + other.inches

        return measure(feet, inches)

    def __sub__(self, other):

        feet = self.feet - other.feet

        inches = self.inches - other.inches

        if inches < 0:

            feet = feet - 1

            inches = 12 + inches

        return measure(feet, inches)





