import pytest
from pytest_bdd import scenarios, given, when, then
from lab4 import uravnenie

scenarios('uravnenie.feature')

@given('коэффициенты <a>, <b>, <c>')
def set_coefficients(a, b, c):
    global eq
    eq = uravnenie()
    eq.get_coef(a, b, c)

@when('мы решаем уравнение')
def solve_equation():
    global roots
    roots = eq.solve()

@then('корни должны быть <expected_roots>')
def check_roots(expected_roots):
    expected_roots = eval(expected_roots) 
    assert roots == expected_roots
