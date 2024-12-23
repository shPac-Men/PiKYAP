Feature: Решение квадратного уравнения

  Scenario: Два действительных корня
    Given коэффициенты 1, -3, 2
    When мы решаем уравнение
    Then корни должны быть (1.0, 2.0)

  Scenario: Один действительный корень
    Given коэффициенты 1, -2, 1
    When мы решаем уравнение
    Then корни должны быть (1.0)

  Scenario: Два комплексных корня
    Given коэффициенты 1, 0, 1
    When мы решаем уравнение
    Then корни должны быть []

