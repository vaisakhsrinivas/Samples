'''
Given a number of seconds, return the duration in spoken English.

Break the duration into hours, minutes, and seconds.
Skip any zero values.
Use singular or plural as appropriate ("1 hour", "2 hours").
If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes and 3 seconds").
'''


def get_spoken_duration(seconds):

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    units = [(hours,"hour"), (minutes,"minute"), (seconds,"second")]

    parts = [f"{value} {name}{'s' if value != 1 else ''}" for value, name in units if value > 0]

    if not parts:
        return "now"
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + " and " + parts[-1]


print(get_spoken_duration(3723)) #should return "1 hour, 2 minutes and 3 seconds".
print(get_spoken_duration(7295)) #should return "2 hours, 1 minute and 35 seconds".
print(get_spoken_duration(8521)) #should return "2 hours, 22 minutes and 1 second".
print(get_spoken_duration(435)) #should return "7 minutes and 15 seconds".
print(get_spoken_duration(14455)) #should return "4 hours and 55 seconds".
print(get_spoken_duration(72000)) #should return "20 hours".
print(get_spoken_duration(1)) #should return "1 second".