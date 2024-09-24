def input_time(time_unit):
    # check om timer er korrekte
    if time_unit == "hour":
        hour = input("Time: ")
        try:
            hour = int(hour)
        except:
            print("Indtast time som tal")
            return input_time("hour")
        if not verify_hour(hour):
            return input_time("hour")
        return hour
    # check om minut er korrekt
    elif time_unit == "minute":
        minute = input("Minut: ")
        try:
            minute = int(minute)
        except:
            print("Indtast time som tal")
            return input_time("minute")
        if not verify_minute(int(minute)):
            return input_time("minute")
        return minute

def verify_hour(h):
    if 0 <= h <= 23:
        return True
    else:
        print("Indtast time imellem 0 og 23")
        return False
    
def verify_minute(m):
    if 0 <= m <= 59:
        return True
    else:
        print("Indtast time imellem 0 og 59")
        return False

def time_calc(h1, h2, m1, m2):
    hours = h2 - h1
    minutes = m2 - m1
    if hours < 0:
        hours += 24
    if minutes < 0:
        minutes += 60
        hours -= 1
        if hours < 0:
            hours += 24

    return hours, minutes


print("indtast ankomsttime")
aHour = input_time("hour")
print("indtast ankomstminut")
aMinute = input_time("minute")
print("indtast afgangstime")
lHour = input_time("hour")
print("indtast afgangsminut")
lMinute = input_time("minute")

time_stayed = time_calc(aHour, lHour, aMinute, lMinute)

print(f"Du har arbejdet {time_stayed[0]} timer og {time_stayed[1]} minutter.")


