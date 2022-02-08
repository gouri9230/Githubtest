def guess_game():
    secret_word = "Chair"
    count = 1
    while count <=3:
        guess_name = input("Guess the secret word: ")
        if(secret_word == guess_name):
            print("Yay! You guessed it right!. \n You win!")
            break;
        else:
            print("Wrong! You have " + str(3-count) + "guess left!")
            if(count==3):
                print("Oops! You lose!")
                count +=1
                break;
            else:
                count += 1
    
print("*********Welcome to the guessing game!!*********")
print("You get 3 chances to guess the word.")
print("Hint: This thing is commonly found in the living area in the house.")
guess_game()
