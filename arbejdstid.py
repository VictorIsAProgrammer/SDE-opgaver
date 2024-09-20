def verify_time_valid_time(time):
    # check om timer er korrekte
    if time == "hour":
        hour = input()
        try:
            hour = int(hour)
        except:
            print("Indtast time som tal")
            return verify_time_valid_time("hour")
        if not verify_hour(int(hour)):
            return verify_time_valid_time("hour")
        return hour
    # check om minut er korrekt
    elif time == "minute": 
        minute = input()
        try:
            minute = int(minute)
        except:
            print("Indtast time som tal")
            return verify_time_valid_time("minute")
        if not verify_minute(int(minute)):
            return verify_time_valid_time("minute")
        return minute

def verify_hour(h):
    if(h >= 0 and h <= 23):
        return h
    else:
        print("Indtast time imellem 0 og 23")
        return(verify_time_valid_time("hour"))
    
def verify_minute(m):
    if(m >= 0 and m <= 59):
        return m
    else:
        print("Indtast time imellem 0 og 59")
        return(verify_time_valid_time("minute"))


print("indtast ankomsttime")
aHour = verify_time_valid_time("hour")
print("indtast ankomstminut")
aMinute = verify_time_valid_time("minute")
print("indtast afgangstime")
lHour = verify_time_valid_time("hour")
print("indtast afgangsminut")
lMinute = verify_time_valid_time("minute")
# print("test values: aHour = " + str(aHour) + ", lHour = " + str(lHour)) # test

# håndterer ikke hvis ankomst (minut eller time) er højere end afgang.
print("du har arbejdet " + str(lHour - aHour) + " timer og " + str(lMinute - aMinute) + " minutter")