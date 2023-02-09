import pytest


@pytest.mark.parametrize("HDL_input, expected",
                         [(65, "Normal"),
                          (45, "Borderline Low"),
                          (20, "Low")
                          ])
def test_HDL_analysis(HDL_input, expected):
    from blood_calc import HDL_analysis
    # Arrange
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected


@pytest.mark.parametrize("LDL_input, expected",
                         [(195, "Very High"),
                          (165, "High"),
                          (135, "Borderline High"),
                          (100, "Normal")
                          ])
def test_LDL_analysis(LDL_input, expected):
    from blood_calc import LDL_analysis
    # Act
    answer = LDL_analysis(LDL_input)
    # Assert
    assert answer == expected
