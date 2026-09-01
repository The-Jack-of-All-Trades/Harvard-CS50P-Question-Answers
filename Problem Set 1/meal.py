def main():
    time = input()
    total_time = convert(time)
    if 7 <= total_time <= 8:
        print("breakfast time")
    elif 12 <= total_time <= 13:
        print("lunch time")
    elif 18 <= total_time <= 19:
        print("dinner time")


def convert(time):
    if "a.m." in time:
        times = time.replace("a.m.", "").split(":")
        hours = float(times[0]) 
        if hours == 12:
            hours -= 12
        minutes = float(times[1]) / 60
        total_time = hours + minutes
        return total_time
    elif "p.m." in time:
        times = time.replace("p.m.", "").split(":")
        hours = float(times[0])
        if hours in range(1,12):
            hours += 12
        minutes = float(times[1]) / 60
        total_time = hours + minutes
        return total_time
    else:
        times = time.split(":")
        hours = float(times[0])
        minutes = float(times[1]) / 60
        total_time = hours + minutes
        return total_time



if __name__ == "__main__":
    main()
