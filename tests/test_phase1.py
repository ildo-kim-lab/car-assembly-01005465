import pytest

import assembly


@pytest.fixture(autouse=True)
def reset_q0():
    assembly.q0 = 0
    yield
    assembly.q0 = 0


@pytest.mark.parametrize("ans", [1, 2, 3])
def test_is_valid_range_accepts_1_to_3(ans):
    assert assembly.is_valid_range(0, ans) is True


@pytest.mark.parametrize("ans", [-1, 0, 4])
def test_is_valid_range_rejects_out_of_range(ans, capsys):
    assert assembly.is_valid_range(0, ans) is False
    assert "ERROR" in capsys.readouterr().out


@pytest.mark.parametrize(
    "ans, expected_type, expected_message",
    [
        (assembly.SEDAN, assembly.SEDAN, "Sedan"),
        (assembly.SUV, assembly.SUV, "SUV"),
        (assembly.TRUCK, assembly.TRUCK, "Truck"),
    ],
)
def test_select_car_type_sets_q0_and_prints_message(ans, expected_type, expected_message, capsys):
    assembly.select_car_type(ans)

    assert assembly.q0 == expected_type
    assert expected_message in capsys.readouterr().out
