from com.bridgelabz.quantitymeasurement.Feet import Feet
from com.bridgelabz.quantitymeasurement.Yard import Yard
from com.bridgelabz.quantitymeasurement.Inch import Inch
import pytest


# Test_case for Feet
# Test_case1 : comparing two feet value
def test_givenTwoFeetValue_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet


# test_case2 : Comparing Two instance feet variable
def test_givenTwoFeetValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet


# test_Case3 : Comparing one feet value should return false when None
def test_givenOneFeetValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_feet = Feet(0.0)
    assert first_feet is not None
