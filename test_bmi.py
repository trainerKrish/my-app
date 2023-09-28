from bmi import bmi
import pytest


def test_bmi_value():
    assert bmi(4,2) == 703