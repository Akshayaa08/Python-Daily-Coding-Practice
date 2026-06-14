# Match-case Statement (switch) :An alternative to using many 'elif' statements
# execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return"It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"
print(day_of_week())
    
def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False

        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False
print(is_weekend("Saturday"))

def is_weekend(day):
    match day:
        case "Sunday"|"Sunday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday" |"Friday":
            return False
        case _:
            return False
print(is_weekend("Friday"))