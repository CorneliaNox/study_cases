# import math
from typing import Callable

# operators = {
#     "+": lambda x, y: x + y,
#     "-": lambda x, y: x - y,
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x / y,
#     "^": lambda x, y: x ** y,
# }

# primitives = {
#   "is_digit": lambda x: x.isdigit(),
#   "is_constant": lambda x: x in constants.keys(),
# }

# constants = {
#   "PI": math.pi,
#   "E": math.e,
# }

# def calculate():
#     lambda_operator = operators["*"]

#     result = lambda_operator(1, 2)

#     return result

# print(calculate())


# class Operator:
#   def __init__(self, priority: int, lambda_function: Callable, is_unary: bool = False):
#     self.priority = priority
#     self.lambda_function = lambda_function
#     self.is_unary = is_unary

#   def get_priority(self):
#     return self.priority

#   def get_lambda_function(self):
#     return self.lambda_function

#   def is_unary(self):
#     return self.is_unary


# class OperatorRegistry:
#   def __init__(self):
#     self.operators = {
#       "+": Operator(1, lambda x, y: x + y),
#       "-": Operator(1, lambda x, y: x - y, True),
#       "*": Operator(2, lambda x, y: x * y),
#       "/": Operator(2, lambda x, y: x / y),
#       "^": Operator(3, lambda x, y: x ** y),
#     }

#   def get_operator(self, operator: str):
#     return self.operators[operator]

# class BaseExpression:
#     def __init__(self):
#       pass

#     def evaluate(self):
#       pass

#     def __str__(self):
#       pass

# class Expression(BaseExpression):
#   def __init__(self, operator: Operator, left: BaseExpression, right: BaseExpression):
#     super().__init__()

#     self.operator = operator
#     self.left = left
#     self.right = right

#   def evaluate(self):
#     return self.operator.get_lambda_function()(self.left.evaluate(), self.right.evaluate())

#   def __str__(self):
#     return f"({self.left} {self.operator} {self.right})"

# class UnaryExpression(BaseExpression):
#   def __init__(self, operator: Operator, expression: BaseExpression):
#     super().__init__()

#     self.operator = operator
#     self.expression = expression

#   def evaluate(self):
#     return self.operator.get_lambda_function()(self.expression.evaluate())

#   def __str__(self):
#     return f"({self.operator} {self.expression})"

# class IdentifierExpression(BaseExpression):
#   def __init__(self, identifier: str):
#     super().__init__()

#     self.identifier = identifier

#   def evaluate(self):
#     return self.identifier

#   def __str__(self):
#     return self.identifier