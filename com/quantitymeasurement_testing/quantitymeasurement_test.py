import pytest

from com.bridgelabz.quantitymeasurement.QuantityMeasurment import QuantityMeasurement, Length


@pytest.mark.parametrize("first_length, second_length,expected",
                         [
                             (QuantityMeasurement(Length.FEET, 3.0), QuantityMeasurement(Length.YARD, 1.0), True),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.YARD, 1.0), False),
                             (QuantityMeasurement(Length.INCH, 1.0), QuantityMeasurement(Length.YARD, 1.0), False),
                             (QuantityMeasurement(Length.INCH, 36.0), QuantityMeasurement(Length.YARD, 1.0), True),
                             (QuantityMeasurement(Length.YARD, 1.0), QuantityMeasurement(Length.FEET, 3.0), True),
                             (QuantityMeasurement(Length.YARD, 1.0), QuantityMeasurement(Length.INCH, 36.0), True),
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.CM, 5.0), True)
                         ])
def test_givenTwoLengthsUnitValue_WhenCompared_ShouldReturnExpected(first_length, second_length, expected):
    assert QuantityMeasurement.compareto(first_length, second_length) == expected


@pytest.mark.parametrize("first_length, second_length,expected",
                         [
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.INCH, 2.0), 4.0),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.INCH, 2.0), 14.0),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.FEET, 1.0), 24.0),
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.CM, 2.5), 3.0),
                         ])
def test_givenTwoLengthsUnitValue_WhenAdd_ShouldReturnExpectedResult(first_length, second_length, expected):
    assert QuantityMeasurement.addition(first_length, second_length) == expected
