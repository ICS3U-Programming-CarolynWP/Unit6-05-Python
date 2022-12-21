# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/19
# Gets the user input for a list of marks.
# Determines the average using a function.

import lists
import math

# Function to find the average
def calculate_average(list_of_marks):
    # Variable
    sum = 0

    # FOR IN loop to determine the average mark
    for number in list_of_marks:
        sum = sum + number
    number_amount = len(list_of_marks)
    # If there is not an error, return the average. If yes, return -1
    if number_amount == 0:
        return -1
    else:
        average = sum / number_amount
        return average


def main():
    # Variable
    user_list_of_marks = []

    while True:
        user_marks_string = input("Enter your mark (0-100,-1 to stop): ")
        if user_marks_string == "-1":
            break
        # TRY CATCH to turn the string to an int
        try:
            user_marks = int(user_marks_string)

            # To make sure the input is between 0 and 100
            if user_marks < 0 or user_marks > 100:
                print("Please enter a mark between 0-100!")
                continue
            else:
                user_list_of_marks.append(user_marks)
        except Exception:
            print("Please enter an integer!.")

    # calling the function
    average = calculate_average(user_list_of_marks)

    # IF ELSE to check for any errors. Displays the mark back to user
    if average == -1:
        print("Please enter a valid integer")
    else:
        # displaying results
        print("Your average mark is {:.3}%.".format(average))


if __name__ == "__main__":
    main()
