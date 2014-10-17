############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print 'please enter a number in celcius degrees that you want converted to farenheit'

userInput = int(raw_input)
userInput = userInput * 9
userInput = userInput / 5
userInput = userInput + 32

print userInput