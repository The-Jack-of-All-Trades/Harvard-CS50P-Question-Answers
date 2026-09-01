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
            if 0 < day <= 31:
                if 12 >= month > 0:
                    break
                else:
                    continue   
            else:
                continue
        elif "," in date:
            date = date.replace(",", "").split(" ")
            month = date[0]
            day = int(date[1])
            year = int(date[2])
            total = 0
            if month not in months:
                continue
            for themonth in months:
                total += 1
                if themonth == month:
                    month = total
                    break
            if 0 < day <= 31:
                if 12 >= month > 0:
                    break
                else:
                    continue
            else:
                continue
        else:
            continue
    except ValueError:
        continue

print(f"{year}-{month:02}-{day:02}")
