############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.


keepGoing = True
while (keepGoing == True):
    print 'how hot are you?'
    t = int(raw_input())
    print 'have you been to africa? y or n'
    a = raw_input()
    print 'have you been sick in the last 24 hours? y or n'
    s = raw_input()
    
    if t > 105:
        keepGoing = False
        print 'you have a sickness'
    elif t >= 102 and s == "y":
        keepGoing = False
        print 'you have a sickness'
    elif (t >= 100 or s == 'y') and a == 'y':
        keepGoing = False
        print 'you have a sickness'
    else:
        print 'you probably do not have ebola'
    
    print 'are there any more patients? y or n'
    p = raw_input()
    if p == 'n':
        keepGoing = False
    elif p == 'y':
        keepGoing = True
    else:
        print 'please input valid answer'