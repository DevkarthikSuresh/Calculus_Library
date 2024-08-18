#Version: 0.1.0 Alpha
import sympy as sp

h = 1e-5
x = sp.symbols('x')

try:
    expression = input("Enter the function: ")
    a = float(input("Enter the value at which you want the derivative: "))

    fx = sp.sympify(expression)
    f_x_plus_h = fx.subs(x, a + h)
    f_x_minus_h = fx.subs(x, a - h)
    result = (f_x_plus_h - f_x_minus_h) / (2 * h)
    result = result.simplify()
    print(f"The derivative of the function at x = {a} is: {result}")
except sp.SympifyError as e:
    print(f"Error in function expression: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
