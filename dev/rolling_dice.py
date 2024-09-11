# import a random number generator
import random


# function to generate a random number between 0 and 5
def generate_random_number():
    return random.randint(1, 6)

# function to get 2 random numbers
def get_two_dice_numbers():
    return (generate_random_number(), generate_random_number())

# def main function
def main():

    print(get_two_dice_numbers())

    while True:
        user_input = input("Roll the dice? (y/n): ")
        if user_input.lower() == "y":
            print(get_two_dice_numbers())
        elif user_input.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")

# execute main function when this script loads
if __name__ == "__main__":
    main()
