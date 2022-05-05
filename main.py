#
# Author: Dylan Baker
# Date: 1st February 2019
# Description: This program is used to make learners in a college scenario and progress them
#  through 34 weeks. Their statistics can be monitored. The program is built with the
#  techniques used in object oriented programming.
#
# Imports the three learner classes.
from assessment_4_fulltime_obj import *
from assessment_4_parttime_obj import *
from assessment_4_evening_obj import *

# Imports default learner class from main object, not required for creation of normal learners, is being used as
#  default data for the "new_learner" variable.
from assessment_4_obj import Learner
new_learner = Learner(1, 80, 80)


# Main definition
def mainmenu():
    display_options_menu()
    choice = select_choice_option()
    global new_learner

    if choice == 1:
        create_learner()

    if choice == 2:
        manage_learner(new_learner)


def display_options_menu():
    print("\nLearner Creation & Management Program Main Menu\nWould you like to manage a learner, or make a new one?\n")
    print("1) Create a Learner \n2) Manage a Learner \nPlease select an option from the above menu")


def select_choice_option():
    choice = 0
    valid_option = False
    while not valid_option:

        try:
            choice = int(input("Option Selected: "))

            if choice in (1, 2):
                valid_option = True

            else:
                print("Please enter a valid option")

        except ValueError:
            print("Please enter a valid option")

    return choice


# M
def create_learner():
    display_create_menu()
    choice = select_create_option()
    global new_learner
    n = ""

    if choice == 1:
        new_learner = FullTime()
        n = "Full-Time"

    elif choice == 2:
        new_learner = PartTime()
        n = "Part-Time"

    elif choice == 3:
        new_learner = Evening()
        n = "Evening"

    elif choice == 0:
        n = "No"

    print(n, "Learner Created\n")

    mainmenu()


def display_create_menu():
    print("\nWhat type of learner would you like to make? \n")
    print("1) Full-Time Learner \n2) Part-Time Learner \n3) Evening Learner \n0) Exit to Main Menu")
    print("Please select an option from the above menu")


def select_create_option():
    choice = 0
    valid_option = False
    while not valid_option:

        try:
            choice = int(input("Option Selected: "))

            if choice in (0, 1, 2, 3):
                valid_option = True
            else:
                print("Please enter a valid option")

        except ValueError:
            print("Please enter a valid option")

    return choice


mainmenu()
