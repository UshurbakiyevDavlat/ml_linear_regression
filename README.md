# Linear regression on python.

Linear regression is supervised kind of learning.

Where:

- x is independent variable (example years_of_experience)
- y is dependent variable (example salaries)

Mathematically, linear regression can be described as a formula:

~~~
Y = a + bx
a - intercept
b - slope/coefficient

for multiple linear regression situation is the same but with just more variables
Y = a + b1 * X1 + b2 * X2 + b3 * X3 + ...

In other words, we have more independent variables and their coefficients, that's it.

Also there are polynomial regression which uses linear regression model but transform it

Y = a + b1 * X1 + b2 * X^2 + b3 * X^3 + ...

and in graphic it looks like a curve
~~~

The goal of ML model is to build a best-fitting straight line according to that formula.