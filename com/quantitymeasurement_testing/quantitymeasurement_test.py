from com.bridgelabz.quantitymeasurement.Feet import Feet
from com.bridgelabz.quantitymeasurement.QuantityMeasurment import QuantityMeasurement, Length

import pytest


# case1 : comparing two feet value

def test_givenZeroFtandZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = QuantityMeasurement(Length.FEET, 0.0)
    assert first_feet == second_feet


# case2 : comparing Two instance feet variable
def test_givenTwoFeetValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet


# case3 : comparing one feet value should return false when None
def test_givenZeroFtValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    assert first_feet is not None


# case4 : compared one feet value with float value
def test_givenZeroFeetAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = float(0.0)
    with pytest.raises(AttributeError):
        assert first_feet == second_feet


# case5 : comparing two different feet value
def test_givenZeroFeetandOneFeet_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = QuantityMeasurement(Length.FEET, 1.0)
    assert first_feet != second_feet


# cases for Yard
def test_givenZeroYardandZeroYard_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = QuantityMeasurement(Length.YARD, 0.0)
    assert first_yard == second_yard

def test_givenZeroYardValueandInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD,0.0)
    second_yard = first_yard
    assert first_yard == second_yard
