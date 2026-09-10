class Person:
    def __init__(self, passport: Passport):
        self.name = passport.name
        self.passport = passport

class Passport:
    def __init__(self, number, name, date):
        self.number = number
        self.name = name
        self.date = date

passport = Passport(123, "Alex", 2026)
person = Person(passport)

print(person.passport.name)
print(person.name)
 