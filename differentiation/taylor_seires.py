#Code Version 0.1.1
#Still some work left before it can  work to calculate the actual sum of series.


import sympy as sp


def taylor(expression, n_terms):
    try:
        x = sp.symbols('x')
        a = sp.symbols('a')

        fx = sp.sympify(expression)
        fx_at_a = fx.subs(x, a)

        symbol = fx.free_symbols
        symbol = list(symbol)[0]

        print(f'{fx_at_a} + ', end='')

        for i in range(1, n_terms + 1):
            try:
                f_prime = sp.diff(fx, symbol, i)
                f_prime_at_a = f_prime.subs(x, a)
                print(f'[{f_prime_at_a}] * [(x-a)^{i}]/{i}!  +  ', end='')
            except Exception as e:
                print(f"\nError during differentiation or substitution: {e}")
                break

    except sp.SympifyError as e:
        print(f'Error: {e}')

    except Exception as e:
        print(f'Error:{e}')

taylor('sin(x)', 5,)
