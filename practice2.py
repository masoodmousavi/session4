from math import factorial 


user_inpute = int(input("please enter your number: "))

for i in range(user_inpute):

    if factorial(i) > user_inpute:
        print("this number is not  factorial")
        break
    elif factorial(i) == user_inpute:
        print("this is a factorial number")
        break
    elif factorial(i) < user_inpute:
        continue