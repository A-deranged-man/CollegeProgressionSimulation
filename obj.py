

import random


class Learner:
    """Generic Learner Class"""

    # This is the constructor
    def __init__(self, progress_rate, attendance_need, assessment_need):

        # Set all attributes with initial values.
        self._progression = 0
        self._weeks_studied = 0
        self._progress_rate = progress_rate
        self._attendance_need = attendance_need
        self._assessment_need = assessment_need
        self._status = "Applied"
        self._type = "Generic"

    # Method to report the needs of the learner.
    def requirement(self):

        # Will return a dictionary containing attendance needs and assessment needs.
        return{"Attendance Need": self._attendance_need, "Assessment Need": self._assessment_need}

    # Method designed to report the current states of the learner.
    def report(self):

        # Return a dictionary containing type, status, progression & weeks studied.
        return{"Learner Type": self._type, "Status": self._status, "Relative Progression": self._progression,
               "Weeks Studied": self._weeks_studied}

    # Private method that updates the status of the learner based on progression.
    def _update_status(self):
        if self._progression >= 33:
            self._status = "Achieved"

        elif self._progression >= 17:
            self._status = "B1_complete"

        elif self._progression > 31:
            self._status = "B2_complete"

        elif self._progression > 7:
            self._status = "Induction_Complete"

        elif self._progression > 0:
            self._status = "Enrolled"

        elif self._progression == 0:
            self._status = "Applied"

    # Method used to progress the learner based on its attendance and assessment consumption.
    def progress(self, attendance, assessment):
        if attendance >= self._attendance_need and assessment >= self._assessment_need:

            # Increment progression by progression rate if above parameters are met.
            self._progression += self._progress_rate

        # Increment weeks progressing.
        self._weeks_studied += 1

        # Calls private _update_status function.
        self._update_status()


# Function to automatically progress learners.
def auto_progress(learner, weeks):

    for week in range(weeks):
        attendance = random.SystemRandom().randint(1, 100)
        assessment = random.SystemRandom().randint(1, 100)
        learner.progress(attendance, assessment)


# Function to manually progress a learner.
def manual_progress(learner):
    attendance = 0
    assessment = 0

    valid = False
    while not valid:
        try:
            assessment = int(input("Please enter an assessment percentage value between 1-100: "))
            if 1 <= assessment <= 100:
                valid = True
            else:
                print("This value is not valid, please enter a assessment value between 1-100 ")
        except ValueError:
            print("This value is not valid, please enter a assessment value between 1-100 ")

    valid = False
    while not valid:
        try:
            attendance = int(input("Please enter an attendance percentage value between 1-100: "))
            if 1 <= attendance <= 100:
                valid = True
                print()
            else:
                print("This value is not valid, please enter an attendance value between 1-100 ")
        except ValueError:
            print("This value is not valid, please enter an attendance value between 1-100 ")

    learner.progress(attendance, assessment)


# Private function to display text informing the user of how to operate the program.
def _display_menu():
    print("1) Progress the learner manually over 1 week")
    print("2) Progress the learner automatically over 34 weeks")
    print("3) Report status of the learner")
    print("0) Return to Learner Menu \n \n")
    print("Please select an option from the above menu.")


# Private function to get the choice of the user.
def _get_menu_choice():
    choice = 0
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 4:
                valid = True
            else:
                print("This value is not valid")
        except ValueError:
            print("This value is not valid")
    return choice


# Function to load  learner management menus
def manage_learner(learner):
    print("\nThis is the Learner Management Menu \n")
    no_exit = True
    while no_exit:

        # Load _display_menu function
        _display_menu()

        # Set option as returned value from _get_menu_choice function
        option = _get_menu_choice()

        # Print a newline
        print("\n")

        # Launch manual_progress function
        if option == 1:
            manual_progress(learner)

        # Launch auto_progress function with week input
        elif option == 2:
            auto_progress(learner, 34)

        # Run learner report function
        elif option == 3:
            print(learner.report())

        # Print message to leaving user.
        elif option == 0:
            print("\nExiting Learner Management Menu. Returning to Main Menu.")
            import assessment_4_main
            assessment_4_main.mainmenu()

