
#reading user inputs and check if the number is odd or even
#find last digit from the user input & first digit
                                          #first digit      import math
                                          #digits = (int)(math.log10(userInput)) 
                                          #firstDigit = (int)(userInput / pow(10, digits))
# in this case i ll be using last digit
userInput=int(input("Enter a number :"))
getlastdigits=(userInput % 10)

if  (userInput% 2 ) == 0:
    print("{0} is Even".format(userInput))
else:
  print("{0} is Odd".format(userInput))

print(getlastdigits,"is your last digit")
