# !/usr/bin/env python3
# Created by: Angel
# Created on April 2,2025
# This program asks the user how many croissants
# they want and if they buy less than 6 croissants,
# they will pay HST(tax) and if they buy 6 or more croissants,
# they do not pay HST.

import constants


def main():
    try:

        # ask the user for how many croissants they want
        num_croissants = int(input("Enter the number of croissants"))
        if num_croissants < 0:  # the number of croissants is less than 0
            print("Number of croissants cannot be negative")

        else:  # If not
            subtotal = num_croissants * constants.COST_OF_EACH_CROISSANTS

        if num_croissants < 6:  # If the user buys less
            # than 6, we add HST
            tax = subtotal * constants.HST  # Calculate the tax
            total = subtotal + tax  # # Add the tax to get total

            print(f"Subtotal: ${subtotal:.2f}")  # Display the subtotal
            # to two decimal places
            print(f"HST: ${tax:.2f}")  # Display the HST
            # to two decimal places
            print(f"Total: ${total:.2f}")  # Display the subtotal
            # to two decimal places

        else:
            print(f"Subtotal: ${subtotal:.2f}")  # Display the subtotal
            # to two decimal places
            print(f"No HST applied")  # Shows that no HST was used
            print(f"total: ${subtotal:.2f}")  # Display the subtotal
            # to two decimal places

    except (ValueError, TypeError):  # This will catch potential error in the program.
        print("Invalid number of croissants.")


if __name__ == "__main__":
    main()
