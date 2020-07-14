from time import localtime

activities = {8: 'sleeping',
              9: 'commuting',
              17: 'working',
              18: 'commuting',
              20: 'eating',
              22: 'resting'}

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print('Unknown, AFK or sleeping!')
