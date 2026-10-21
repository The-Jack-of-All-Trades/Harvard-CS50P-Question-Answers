def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") # .2f will round the tip to 2 decimal places

# Requires an input then gets rid of the dollar sign and returns a float of that value
def dollars_to_float(d):
    d = d.replace("$", " ")
    return float(d)

# Requires an input then gets rid of the percent sign
def percent_to_float(p):
    p = p.replace("%", " ")
    p = float(p) / 100 # simple equation to find the percent of p while also converting p to a float
    return float(p)
   

main()
