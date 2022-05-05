
from assessment_4_obj import *


class FullTime(Learner):
    """ Full-Time learner """

    # Constructor
    def __init__(self):
        # Call the parent class constructor with default values for a learner.
        # progress_rate , attendance_need , assessment_need
        super().__init__(1, 80, 80)
        self._type = "Full-Time"

    # Make a variation of the "progress" function
    def progress(self, attendance, assessment):
        if attendance >= self._attendance_need and assessment >= self._assessment_need:

            # Increment progression by progression rate.
            self._progression += self._progress_rate

        # Increment weeks progressing.
        self._weeks_studied += 1

        # Calls private _update_status function.
        self._update_status()
