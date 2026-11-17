"""Task 1: tests INSIDE the file (doctest).

The rule (this is the specification):
  * a year divisible by 4 is a leap year,
  * except a year divisible by 100: that is NOT a leap year,
  * except a year divisible by 400: that IS a leap year again.
"""


def is_leap_year(year):
    """Return True if the year has 366 days.

    Each >>> line is a test. Python runs it and
    checks the result on the next line.

    >>> is_leap_year(2024)
    True
    >>> is_leap_year(1900)
    False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
