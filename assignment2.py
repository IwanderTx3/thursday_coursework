user_input = 'y'

while user_input.casefold() == 'y' :

    word = str(input("enter a word "))
    drow = word[::-1]

    if drow.casefold() == word.casefold():
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is NOT a palindrome.") 
    user_input = input("Would you like to do another? (y or n) ")
    
print("Thank you!")

