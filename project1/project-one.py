# Convert time from input to hours, days, and minutes

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


def timeConverter(secondsIn):
    seconds = secondsIn  # % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    print(f'{hours} hours')
    print(f'{minutes} minutes')
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
