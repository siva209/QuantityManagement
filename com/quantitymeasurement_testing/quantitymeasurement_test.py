from com.bridgelabz.quantitymeasurement.Feet import Feet
from com.bridgelabz.quantitymeasurement.QuantityMeasurment import QuantityMeasurement, Length

import pytest


# UC3 : 2in = 5cm
def test_givenTwoInchAndFiveCMValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 2.0)
    second_cm = QuantityMeasurement(Length.CM, 5.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_cm
