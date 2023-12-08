# Task 2
# program that displays a logical error.

# Number guessing game with hints 


def game ():

    print()
    print("GUESS THE NUMBER (in 6 or less guesses)")
    print()

    # define counting integer.

    n = 0

    # Import random module
    # Generate random number between 0 and 50.

    import random

    rand_num = random.randint(0,50)

    while True:

        # define integer, prompt user input.

        try:

            print()
            num_1 = int(input("Please enter a number between 0 and 50: "))
            n += 1

        # Resart loop if something else than a number is entered.

        except:

            print()
            print("Please enter a valid number")

            continue

        # Restart loop if a number out of range is entered

        else:
            if(num_1 < 0 or num_1 > 50):
                print()
                print("Number out of range, try again.")
                n -= 1
                continue

            # Restart the loop if the number entered is not equal to rand_num.

            if (num_1 != rand_num):
                print()
                print ("Sorry, Try again")  

                # Give a hint each try.

                if (n == 1 and rand_num % 2 == 1):
                    print()
                    print("Hint: its an odd number.")

                elif (n == 1 and rand_num % 2 == 0):
                    print()
                    print("Hint: its an even number")

                if (n > 1 and n < 6  and rand_num < num_1):
                    print()
                    print("Hint: your number is to high.")

                elif (n > 1 and n < 6 and rand_num > num_1):
                    print()
                    print("Hint: your number is too low")

            # stop the loop if user tries more than 6 times

                if (n >= 6):

                    print()
                    print("You lost")
                    print()
                    print(f"The number is: {rand_num}")
                    print()
                    play_ans = input ("Try again? Please enter 'Y' for yes or 'N' for no: ")

                    # Restart program if user wants to play again.

                    if (play_ans == "Y" or play_ans == "y"):
                        game()

                # stop the program if the user doen't want to play again

                    if (play_ans == "N" or play_ans == "n"):
                        print()
                        print("Goodbye!")
                    break

         # Stop the loop if the correct number is entered.

            else:

                print()
                print(f"Congratulations! you've guessed right after {n} attempt(s)")
                print()

                # Restart the program if the user wants to play again

                play_ans_2 = input("would you like to play again? Enter 'Y' for yes and 'N' for no: ")

            
                if (play_ans_2 == "Y" or play_ans_2 == "y"):
                    game()

                # Stop the program if the user doesn't want to play again

                if (play_ans_2 == "N" or play_ans_2 == "n"):
                    print ()
                    print("Goodbye!")                
                break
# run the program
game()


    
    

    




