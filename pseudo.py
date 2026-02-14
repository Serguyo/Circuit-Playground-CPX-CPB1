print("Starting Code Challenge")


user_input = input("Enter an integer number 20 or greater > ")

try:
    user_number = int(user_input)

    if user_number >= 20:
        print("Your number", user_number, "is a valid Integer 20 or greater. Thanks")
        print("Starting While Loop - Print Count Variable")
        print("The user input started as", user_number)

        count = 10

        while user_number > 1:
            user_number = user_number / 2
            count = count / 2

            print("The current value of the user input after some math is", user_number)
            print("The while loop has looped", count, "time")

        print("Ending While Loop")
        print("The While Loop, looped a total of", count, "times")
        print("Ending Code Challenge")

    else:
        print("Error: Number must be 20 or greater.")

except:
    print("Wrong! That is not a valid integer.")
