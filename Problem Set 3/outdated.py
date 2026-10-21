months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

while True:
    try:
        date = input("Date: ")
        if "/" in date: # Splits the date into a list of month, day, year, as assigns them the corresponding variables
            date = date.split("/") 
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])
            if 0 < day <= 31: 
                if 12 >= month > 0: # If the day in between 0 and 31 and the month is between 0 and 12, exit the "while True" loop
                    break
                else:
                    continue   
            else:
                continue
        elif "," in date: # Replaces the "," in the input to nothing, then creates a list using the ".split()" method
            date = date.replace(",", "").split(" ")
            month = date[0] # Month will be a string, not an integer
            day = int(date[1])
            year = int(date[2])
            total = 0
            if month not in months: # If the month that is input by the user is not in the list "months" shown in line 1, then prompt the user again
                continue
            for themonth in months: # Add 1 to total until the name of the month input by the user equals the month in the list "months," then set month to a number and exit the loop
                total += 1
                if themonth == month:
                    month = total
                    break
            if 0 < day <= 31: # The exact same block of code written as shown in line 25
                if 12 >= month > 0:
                    break
                else:
                    continue # Just a bunch of else statements and a ValueError except block statement to reprompt the user if the if blocks were not true
            else:
                continue
        else:
            continue
    except ValueError: 
        continue

print(f"{year}-{month:02}-{day:02}") # Round the month and the day to 2 decimal places and print the date in this format
