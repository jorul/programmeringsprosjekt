"""Operator"""
import numbers


class Operator:
    """class handling operators"""
    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def execute(self, number1, number2, debug=True):
        """Check type"""
        if not isinstance(number1, numbers.Number) or not isinstance(number2, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.operation(number1, number2)
        if debug is True:
            print("Operation: " + self.operation.__name__ + "({:f}, {:f}) = {:f}".format(number1, number2, result))
        return result
