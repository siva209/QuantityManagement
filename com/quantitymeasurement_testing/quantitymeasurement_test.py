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

# testcase4 : Compared one feet value with float value
def test_givenOneFeetAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = float(0.0)
    with pytest.raises(AssertionError):
        assert first_feet == second_feet


# testcase5 : Comparing two different feet value
def test_givenTwoDifferentFeetValue_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(0.0)
    second_feet = Feet(1.0)
    assert first_feet != second_feet



# Test_case for Yard
def test_givenTwoYardValue_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(0.0)
    second_yard = Yard(0.0)
    assert first_yard == second_yard

def test_givenTwoYardValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(0.0)
    second_yard = first_yard

