user_input = 'y'

while user_input.casefold() == 'y' :

    num = int(input("Please enter a number to check for prime: "))
    if num > 1:
        for check in range(2,num):
            if (num % check) == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")

    user_input = input("Would you like to do another? (y or n) ")
    
print("Thank you!")

