import random

numbers = [1, 2, 4, 9, 20, 36, 45, 100, 625, 999, 1000]
hints = ["The  number which is neither prime nor composite.", "The even prime number.",
         "The smallest composite number.", "The square root of 81.", "The value of 4x5.", "The square of 6.",
         "The result of 5x9.", "The smallest 3 digit number.", "The square of 25.", "The largest 3 digit number.",
         "The cube of 10."]


def logic(total_score):
    print("\nPresent Score = ", total_score)
    x = random.randint(0, 10)
    print("\nGuess the correct number")
    print("\nHint :", hints[x])
    inp = int(input("Enter number"))
    if inp == numbers[x]:
        print("\nCorrect Answer.")
        total_score = total_score + 10
    else:
        total_score = total_score - 10
        print("\nWrong Answer.")
    return total_score


def game():
    print("***WELCOME TO THE NUMBER GUESSING GAME***")
    total_score = 100
    total_score = logic(total_score)
    ch = True
    while total_score > 0 and ch:
        choice = int(input("\nDo you wish to play again?(1 for YES/ 0 for N)"))
        if choice == 1:
            total_score = logic(total_score)
        elif choice == 0:
            print("\nFinal Score : ", total_score)
            exit()
        else:
            ch = False
    if total_score == 0:
        print("\nFinal Score:", total_score)
        print("\nGame Over. You have lost.\n")
        exit()


game()