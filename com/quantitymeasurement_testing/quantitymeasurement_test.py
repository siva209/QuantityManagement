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