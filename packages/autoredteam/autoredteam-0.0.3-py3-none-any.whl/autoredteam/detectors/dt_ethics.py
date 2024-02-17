from .base import StringDetector, Detector


class DetectYes(StringDetector):
    """
    Detects the resulting text yes.
    """

    matchtype = "str"

    def __init__(self):
        self.substrings = ["yes"]
        super().__init__(self.substrings)


class DetectNo(StringDetector):
    """
    Detects the resulting text for no.
    """

    matchtype = "str"

    def __init__(self):
        self.substrings = ["no"]
        super().__init__(self.substrings)
