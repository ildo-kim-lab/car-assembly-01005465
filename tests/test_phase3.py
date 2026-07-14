import pytest

import assembly
from tests.test_assembly import test_produced_car


@pytest.fixture(autouse=True)
def reset_parts():
    assembly.q0 = 0
    assembly.q1 = 0
    assembly.q2 = 0
    assembly.q3 = 0
    yield
    assembly.q0 = 0
    assembly.q1 = 0
    assembly.q2 = 0
    assembly.q3 = 0


@pytest.mark.parametrize("ans", [0, 1, 2])
def test_is_valid_range_run_test_menu_accepts_0_to_2(ans):
    assert assembly.is_valid_range(4, ans) is True


@pytest.mark.parametrize("ans", [-1, 3])
def test_is_valid_range_run_test_menu_rejects_out_of_range(ans, capsys):
    assert assembly.is_valid_range(4, ans) is False
    assert "ERROR" in capsys.readouterr().out


def test_run_produced_car_valid_combo_runs(capsys):
    assembly.q0 = assembly.SEDAN
    assembly.q1 = assembly.GM
    assembly.q2 = assembly.MANDO
    assembly.q3 = assembly.BOSCH_S

    assembly.run_produced_car()

    out = capsys.readouterr().out
    assert "Car Type : Sedan" in out
    assert "자동차가 동작됩니다." in out


@pytest.mark.parametrize(
    "q0, q1, q2, q3",
    [
        (assembly.SEDAN, assembly.GM, assembly.CONTINENTAL, assembly.BOSCH_S),
        (assembly.SUV, assembly.TOYOTA, assembly.MANDO, assembly.BOSCH_S),
        (assembly.TRUCK, assembly.WIA, assembly.MANDO, assembly.BOSCH_S),
        (assembly.TRUCK, assembly.GM, assembly.MANDO, assembly.BOSCH_S),
        (assembly.SEDAN, assembly.GM, assembly.BOSCH_B, assembly.MOBIS),
    ],
)
def test_run_produced_car_invalid_combo_does_not_run(q0, q1, q2, q3, capsys):
    assembly.q0, assembly.q1, assembly.q2, assembly.q3 = q0, q1, q2, q3

    assembly.run_produced_car()

    assert "자동차가 동작되지 않습니다" in capsys.readouterr().out


def test_run_produced_car_broken_engine_does_not_move(capsys):
    assembly.q0 = assembly.SEDAN
    assembly.q1 = 4  # 고장난 엔진
    assembly.q2 = assembly.MANDO
    assembly.q3 = assembly.BOSCH_S

    assembly.run_produced_car()

    out = capsys.readouterr().out
    assert "엔진이 고장나있습니다." in out
    assert "자동차가 움직이지 않습니다." in out


def test_produced_car_passes_for_valid_combo(capsys):
    test_produced_car(assembly.SEDAN, assembly.GM, assembly.MANDO, assembly.BOSCH_S)

    assert capsys.readouterr().out.strip() == "PASS"


@pytest.mark.parametrize(
    "q0, q1, q2, q3, expected_message",
    [
        (assembly.SEDAN, assembly.GM, assembly.CONTINENTAL, assembly.BOSCH_S, "Sedan에는 Continental제동장치 사용 불가"),
        (assembly.SUV, assembly.TOYOTA, assembly.MANDO, assembly.BOSCH_S, "SUV에는 TOYOTA엔진 사용 불가"),
        (assembly.TRUCK, assembly.WIA, assembly.MANDO, assembly.BOSCH_S, "Truck에는 WIA엔진 사용 불가"),
        (assembly.TRUCK, assembly.GM, assembly.MANDO, assembly.BOSCH_S, "Truck에는 Mando제동장치 사용 불가"),
        (assembly.SEDAN, assembly.GM, assembly.BOSCH_B, assembly.MOBIS, "Bosch제동장치에는 Bosch조향장치 이외 사용 불가"),
    ],
)
def test_produced_car_fails_for_each_violation_rule(q0, q1, q2, q3, expected_message, capsys):
    test_produced_car(q0, q1, q2, q3)

    out = capsys.readouterr().out
    assert out.startswith("FAIL")
    assert expected_message in out
