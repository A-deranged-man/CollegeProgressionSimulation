

from assessment_4_obj import *


class Evening(Learner):
    """ Part-Time learner """

    # Constructor
    def __init__(self):
        # Call the parent class constructor with default values for a learner.
        # progress_rate , attendance_need , assessment_need
        super().__init__(1, 80, 80)
        self._type = "Evening"

    # Make a variation of the "progress" function
    def progress(self, attendance, assessment):
        if attendance >= self._attendance_need and assessment >= self._assessment_need:

            # Increment progression by progression rate quartered.
            self._progression += self._progress_rate - 0.75

        # Increment weeks progressing.
        self._weeks_studied += 1

        # Calls private _update_status function.
        self._update_status()
