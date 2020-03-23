# ASSIGNMENT: Convert time from input to hours, days, and minutes

# 0 . Display welcome message
welcomeMessage = 'Welcome to the Time Conversion Calculator!'
print(welcomeMessage)

# 1. Prompt user for hours, minutes, seconds
# TODO: Prompt for minutes and hours
# prompt for seconds and cast to integer
hoursInput = input("Enter a number of hours: ")
minutesInput = input("Enter a number of minutes: ")
secondsInput = input("Enter a number of seconds: ")

# cast to integer
hoursInput = int(hoursInput)
minutesInput = int(minutesInput)
secondsInput = int(secondsInput)

# 2. Calculate Time

# convert to seconds

hoursToSeconds = hoursInput * 3600
minToSeconds = minutesInput * 60

# add them together

totalSeconds = hoursToSeconds + minToSeconds + secondsInput

# https://www.geeksforgeeks.org/converting-seconds-into-days-hours-minutes-and-seconds/


def timeConverter(secondsIn):
    day = secondsIn // (24 * 3600)
    remainder = secondsIn % (24 * 3600)
    hour = remainder // 3600
    remainder %= 3600
    minutes = remainder // 60
    remainder %= 60
    seconds = remainder

    # handle all zeros
    if (day == 0) and (hour == 0) and (seconds == 0):
        return print("No time units to report.")
    # handle days and 0 days
    if day > 0:
        if day == 1:
            print(f'{day} day')
        else:
            print(f'{day} days')
    if hour > 0:
        if hour == 1:
            print(f'{hour} hour')
        else:
            print(f'{hour} hours')
    if minutes > 0:
        if minutes == 1:
            print(f'{minutes} minute')
        else:
            print(f'{minutes} minutes')
    if seconds > 0:
        if seconds == 1:
            print(f'{seconds} second')
        else:
            print(f'{seconds} seconds')


# 3. Output results
print()  # blank line
print("Your time conversion is:")
timeConverter(totalSeconds)
print("Goodbye!")


# 4. Test edge cases
# enter zeros for any time unit
# enter all zeros
# minute and minutes for output
