# python countdown timer
# import time module and its one of the function "self"

import time
my_time = int(input("Enter the timer in seconds: "))# ask the user how long would they like to set the timer

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) #after each iteration it will sleep for one second

print("Time's up")




