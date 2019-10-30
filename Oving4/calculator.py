"""Calculator"""
import re
import numbers
import numpy
from function import Function
from operatoren import Operator
from container import Queue, Stack


class Calculator():
    def __init__(self):
        # Define the functions supported by linking them to Python
        # functions. These can be made elsewhere in the program,
        # or imported (e.g., from numpy)
        self.functions = {'EXP': Function(numpy.exp),
                          'LOG': Function(numpy.log),
                          'SIN': Function(numpy.sin),
                          'COS': Function(numpy.cos),
                          'SQRT': Function(numpy.sqrt)
                          }
        # Define the operators supported
        # Link them to Python functions (here: from numpy)
        self. operators = {'PLUSS': Operator(numpy.add, 0),
                           'GANGE': Operator(numpy.multiply, 1),
                           'DELE': Operator(numpy.divide, 1),
                           'MINUS': Operator(numpy.subtract, 0)
                           }
        # Define the output−queue . The parse text method fills this with RPN.
        # The evaluate_output_queue method evaluates it
        self.output_queue = Queue()
        self.input_queue = Queue()

    def evaluate_output_queue(self):
        if not isinstance(self.output_queue.peek(), Function) and not isinstance(self.output_queue.peek(), Operator):
            raise TypeError("This is not RPN")

    def RSAcalculation(self):
        sta = Stack()
        size = self.output_queue.size()
        for i in range(0, size):
            element = self.output_queue.pop()
            if isinstance(element, numbers.Number):
                sta.push(element)
            elif isinstance(element, Function):
                number = sta.pop()
                sta.push(element.execute(number))
            else: #element er operator
                number2 = sta.pop()
                number1 = sta.pop()
                sta.push(element.execute(number1, number2))
        return sta.pop()

    def to_RPN(self):
        op_stack = Stack()
        size_input = self.input_queue.size()
        for i in range(0, size_input):
            element = self.input_queue.peek()
            if isinstance(element, numbers.Number):
                self.output_queue.push(self.input_queue.pop())
            elif isinstance(element, Function):
                op_stack.push(self.input_queue.pop())
            elif element == "(":
                op_stack.push(self.input_queue.pop())
            elif element == ")":
                el = op_stack.peek()
                while el != "(":
                    self.output_queue.push(op_stack.pop())
                    el = op_stack.peek()
                op_stack.pop()
                self.input_queue.pop()
            elif isinstance(element, Operator):
                if not op_stack.is_empty():
                    el = op_stack.peek()
                    while (isinstance(el, Operator) and el.strength >= element.strength) or isinstance(el, Function):
                        self.output_queue.push(op_stack.pop())
                        if op_stack.is_empty():
                            break
                        el = op_stack.peek()
                op_stack.push(self.input_queue.pop())
        size_stack = op_stack.size()
        for i in range(0, size_stack):
            self.output_queue.push(op_stack.pop())

    def textparser(self, input_txt):
        txt = input_txt.replace(" ", "").upper()
        nums = "^[-0123456789.]+"
        funcs = "|".join(["^" + func for func in self.functions])
        ops = "|".join(["^" + op for op in self.operators])
        parenths = r"^[\(\)]"
        while txt != "":
            check = re.search(nums, txt)
            if check is not None:
                txt = self.sub_string(txt, check.end)
                self.input_queue.push(float(check.group(0)))
            check = re.search(funcs, txt)
            if check is not None:
                txt = self.sub_string(txt, check.end)
                self.input_queue.push(self.functions[check.group(0)])
            check = re.search(ops, txt)
            if check is not None:
                txt = self.sub_string(txt, check.end)
                self.input_queue.push(self.operators[check.group(0)])
            check = re.search(parenths, txt)
            if check is not None:
                txt = self.sub_string(txt, check.end)
                self.input_queue.push(check.group(0))

    def sub_string(self, string, end):
        if len(string)-1 < end(0):
            return ""
        return string[end(0):]

    def calculate_expression(self, txt):
        self.textparser(txt)
        self.to_RPN()
        return self.RSAcalculation()
