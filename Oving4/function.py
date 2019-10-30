"""Function"""
import numbers


class Function:
    """Class handling functions"""
    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        """Check type"""
        if not isinstance(element, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)
        if debug is True:
            print("Function: " + self.func.__name__ + "({:f}) = {:f}".format(element, result))
        return result
