from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"
    
    def say_birthday(self):
        month_values = ["January", "Febuary", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "December"]

        day = self._birthday.get_day()
        month = self._birthday.get_month()

        if 10 <= day % 100 <= 20:
            day_suffix = "th"
        elif day % 10 == 1:
            day_suffix = "st"
        elif day % 10 == 2:
            day_suffix = "nd"
        elif day % 10 == 3:
            day_suffix = "rd"
        else:
            day_suffix = "th" 
        return f"{day}{day_suffix} of {month_values[month - 1]}"

    def __lt__(self,other):
        return self.first_name < other.first_name
    

T = Person("Ben", "Hansen")
T.set_birthday(6, 23)
print(T.say_birthday())