from datetime import datetime as dt
SHORT_MONTH = (4, 6, 9, 11)
EOM = (30, 31)  # eom = end of month
FEB_EOM = (28, 29, 30, 31)  # eom = end of month
# 1. DateManager takes integers as inputs (for example 1) and finds the date the next month
# 2. DateManager is for the date_to and date_from tequila queries which are 2 and 3 months from today's date


class DateManager:
    def __init__(self, months_ahead):
        self.now = dt.now()
        self.months_ahead = months_ahead
        self.month = ""
        self.day = ""
        self.year = ""
        self.month_calculator()

    def month_calculator(self):
        # generates month
        if self.now.month + self.months_ahead <= 12:
            self.month = int(self.now.month) + self.months_ahead
        else:
            self.month = ("0" + str(self.now.month - 12 + self.months_ahead))
            if self.month == "010":
                self.month = 10
        self.day_calculator()

    def day_calculator(self):
        # checks day is correct - ignores leap years (only once every 4 years)
        if self.month == 2 and self.now.day == FEB_EOM:
            self.day = 28
        elif self.month == SHORT_MONTH and self.now.day == EOM:
            self.day = 30
        else:
            self.day = self.now.day
        self.year_calculator()

    def year_calculator(self):
        # generates year
        if self.now.month >= 11:
            self.year = int(self.now.year) + 1
        else:
            self.year = self.now.year

    def date_calculator(self):
        self.months_ahead = 0
        return f"{self.day}/{self.month}/{self.year}"
