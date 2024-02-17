from .base import StringDetector, Detector


class DetectPositive(StringDetector):
    """
    Detects the resulting text in the positive.
    """

    matchtype = "str"

    def __init__(self):
        self.substrings = ["positive"]
        super().__init__(self.substrings)


class DetectNegative(StringDetector):
    """
    Detects the resulting text in the negative.
    """

    matchtype = "str"

    def __init__(self):
        self.substrings = ["negative"]
        super().__init__(self.substrings)
