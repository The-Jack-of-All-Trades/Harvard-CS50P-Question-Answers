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
        if "/" in date:
            date = date.split("/")
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])
            if 31 >= day > 0 and 12 >= month > 0:
                break
            else:
                continue
        elif "," in date:
            date = date.replace(",", "").split(" ")
            month = date[0]
            day = int(date[1])
            year = int(date[2])
            if month not in months:
                continue
            month_count = 0
            for themonth in months:
                month_count += 1
                if month == themonth:
                    month = month_count
                    break
            if 31 >= day > 0 and 12 >= month > 0:
                break
            else:
                continue
        else:
            continue
    except ValueError:
        continue

print(f"{year}-{month:02}-{day:02}")
