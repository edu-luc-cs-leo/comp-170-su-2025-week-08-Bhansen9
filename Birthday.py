from datetime import datetime

class Birthday:

    # Some data for this object: the number of days in each month.
    # For simplicity, we ignore leap years and keep February at 28.
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        """Basic constructor. It validates the arguments past to it
        and if they are out of range, it assigns a default value of
        January 1."""
        # Protect month value
        if month >= 1 and month <= 12:
            self.__month = month
        else:
            # In case of out of range month, default to January
            self.__month = 1
        # At this point we have a legit month value 1-12.
        # Protect day value; use -1 in array to synchronize months
        if day >= 1 and day <= Birthday.days_in_month[month - 1]:
            self.__day = day
        else:
            # In case of out of range day, default is 1st of month
            self.__day = 1
    # end basic constructor

    def set_day(self, day):
        """Mutator for day. It only changes the day value if the
        passed argument is within a valid range for the given month."""
        if day > 0 and day <= Birthday.days_in_month[self.__month-1]:
            self.__day = day
    # end set_day


    def set_month(self, month):
        #make sure the the month is set to a correct month
        if month > 0 and month <= 12:
            self.__month = month

    # Accessor for __month
    def get_month(self):
        return self.__month

    # Accessor for __day
    def get_day(self):
        return self.__day




        # COMPLETE THIS FOR YOUR ASSIGNMENT
        
    def day_in_year(self, month, day):
        """calculates the day number within the year corresponding to a given 
        date (month, day), assuming that February has 28 days always."""
        count = 0
        for i in range(month-1):
            count += Birthday.days_in_month[i]
        return count + day

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.get_month()}/{self.get_day()} ]"
    
     # Compute days to birthday
    def days_until(self):
        # obtain today's date
        # extract month and day
        # subtract from birthday
        # return # of days

        #collect todays data
        today = datetime.today()
        #find the days count for the data just collected
        count_Today = 0
        for i in range(today.month-1):
            count_Today += Birthday.days_in_month[i]
        count_Today += today.day
# find the days count for the birthday in question
        count_Target = 0
        for i in range(self.__month-1):
            count_Target += Birthday.days_in_month[i]
        count_Target += self.__day
#return the right count and how many days are remaining
        return count_Target - count_Today if count_Target >= count_Today else 365 + (count_Target - count_Today)

    
demo = Birthday(7, 22)

print(demo.days_until())

# print(demo.days_until())
# print(demo.day_in_year(6,29)) # d_b
# print(demo.day_in_year(4,29)) # d_t