def main():
    time = input() # User will just type something on a blank terminal 
    total_time = convert(time) # Passing in the input into the called function "convert()"
    if 7 <= total_time <= 8:
        print("breakfast time")
    elif 12 <= total_time <= 13:
        print("lunch time")
    elif 18 <= total_time <= 19:
        print("dinner time")

# Takes user input called time
def convert(time):
    if "a.m." in time: # Only if it has "a.m." in the input, it will replace the "a.m." with nothing then split the input at ":"
        times = time.replace("a.m.", "").split(":") 
        hours = float(times[0]) # "times[0]" is just the first value in the times list created by the ".split()" method
        if hours == 12: # Because we are going my military time, we need to subtract 12 from 12 in order to get 0 which is midnight
            hours -= 12
        minutes = float(times[1]) / 60 # Simple equation to find the minutes, "times[1]" in the second value in the times list created by the ".split()" method
        total_time = hours + minutes
        return total_time
        
    elif "p.m." in time: # Only if it had "p.m." in the input, it will replace the "p.m." with nothing then split the input at the ":"
        times = time.replace("p.m.", "").split(":")
        hours = float(times[0])
        if hours in range(1,12): # Any hour in this range will have the same effect put in place on it
            hours += 12
        minutes = float(times[1]) / 60
        total_time = hours + minutes
        return total_time
        
    else: # This will be anything else that does not have a "a.m." or a "p.m."
        times = time.split(":") 
        hours = float(times[0])
        minutes = float(times[1]) / 60
        total_time = hours + minutes
        return total_time


# Not currently learned in this unit, more on it later
if __name__ == "__main__":
    main()
