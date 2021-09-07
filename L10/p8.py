#wapp to generate a random motivational message

#S1-create a list of motivational msgs 
msg = ["all is well","just do it","think twice code once","never quit","be bold","be +ve","failing to plan is planning to fail"]

#S2- generate a random integer
import random
r = random.randrange(len(msg))

#S3-use random integer to select one of the msgs and print
print(msg[r])