#!/usr/bin/env python3
# if, elif, else - A simple program to calculate your grade

message = 'It looks like.... '

# promt user for score
score = float(input("What did you get on the Linux exam?"))

# input value for grades 
if score >= 90 :
    message = message + 'Cool you got an A.'
elif score >= 80:
    message = message + 'Cool you got a B.'
elif score >= 70:
    message = message + 'Cool you got a C.'
elif score < 70:
    message = message + 'Better luck next time.'
elif score > 100:
    message = message + 'You cannot get more than 100.'
else:
    message = message + 'Invalid input.'
print(message)

