# Gyldige værdier for timer og minutter
MIN_HOUR, MAX_HOUR = 0, 23
MIN_MINUTE, MAX_MINUTE = 0, 59


def input_time(time_unit):
    while True:
        if time_unit == "hour":
            user_input = input("Indtast time: ")
            try:
                hour = int(user_input)
                if verify_hour(hour):  # Kontrollerer om timen er gyldig
                    return hour
                else:
                    print("Indtast en time mellem 0 og 23.")
            except ValueError:
                print("Indtast timer som et heltal.")

        elif time_unit == "minute":
            user_input = input("Indtast minut: ")
            try:
                minute = int(user_input)
                if verify_minute(minute):  # Kontrollerer om minuttet er gyldigt
                    return minute
                else:
                    print("Indtast et minut mellem 0 og 59.")
            except ValueError:
                print("Indtast minutter som et heltal .")

# Tjekker om timen er inden for det gyldige interval (0-23)
def verify_hour(h):
    if MIN_HOUR <= h <= MAX_HOUR:
        return True  # Time er gyldig
    else:
        print(f"Indtast time imellem {MIN_HOUR} og {MAX_HOUR}")  # Fejlmeddelelse for ugyldigt interval
        return False


# tjekker om minuttet er inden for det gyldige interval (0-59)
def verify_minute(m):
    if MIN_MINUTE <= m <= MAX_MINUTE:
        return True  # Minut er gyldigt
    else:
        print(f"Indtast minut imellem {MIN_MINUTE} og {MAX_MINUTE}")  # Ugyldigt interval
        return False


# gemmer de udregnede timer og minutter i en fil
def save_to_file(hours, minutes, filename="work_time_log.txt"):
    with open(filename, "a") as file:  # Åbn filen i append-tilstand
        file.write(f"Du har arbejdet {hours} timer og {minutes} minutter.\n")  # Skriv resultatet til filen
    print(f"\nResultatet er gemt i filen: {filename}")  # Bekræftelse til brugeren


# Beregner arbejdstiden baseret på ankomst- og afgangstid
def calculate_work_time(h1, h2, m1, m2):
    hours = h2 - h1  # Forskel i timer
    minutes = m2 - m1  # Forskel i minutter

    # Juster for krydsning af midnat eller negative minut-differencer
    if hours < 0:
        hours += 24  # Juster for krydsning af midnat
    if minutes < 0:
        minutes += 60  # hvis minutter bliver negative, så tilføj 60 min
        hours -= 1  # og træk en time fra
        if hours < 0:
            hours += 24  # Juster, hvis timerne bliver negative

    return hours, minutes  # Returner de beregnede timer og minutter


# main metode. indhenter input, udregner arbejdstid og viser/gemmer resultater
def main():
    # Bed om input
    print("Indtast ankomsttime")
    aHour = input_time("hour")
    print("Indtast ankomstminut")
    aMinute = input_time("minute")
    print("Indtast afgangstime")
    dHour = input_time("hour")
    print("Indtast afgangsminut")
    dMinute = input_time("minute")

    time_stayed = calculate_work_time(aHour, dHour, aMinute, dMinute)

    save_to_file(time_stayed[0], time_stayed[1])

    print(f"Du har arbejdet {time_stayed[0]} timer og {time_stayed[1]} minutter.")


# Kør main
main()