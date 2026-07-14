import pytest

import assembly


@pytest.fixture(autouse=True)
def reset_parts():
    assembly.q1 = 0
    assembly.q2 = 0
    assembly.q3 = 0
    yield
    assembly.q1 = 0
    assembly.q2 = 0
    assembly.q3 = 0


@pytest.mark.parametrize("ans", [0, 1, 2, 3, 4])
def test_is_valid_range_engine_accepts_0_to_4(ans):
    assert assembly.is_valid_range(1, ans) is True


@pytest.mark.parametrize("ans", [-1, 5])
def test_is_valid_range_engine_rejects_out_of_range(ans, capsys):
    assert assembly.is_valid_range(1, ans) is False
    assert "ERROR" in capsys.readouterr().out


@pytest.mark.parametrize("ans", [0, 1, 2, 3])
def test_is_valid_range_brake_accepts_0_to_3(ans):
    assert assembly.is_valid_range(2, ans) is True


@pytest.mark.parametrize("ans", [-1, 4])
def test_is_valid_range_brake_rejects_out_of_range(ans, capsys):
    assert assembly.is_valid_range(2, ans) is False
    assert "ERROR" in capsys.readouterr().out


@pytest.mark.parametrize("ans", [0, 1, 2])
def test_is_valid_range_steering_accepts_0_to_2(ans):
    assert assembly.is_valid_range(3, ans) is True


@pytest.mark.parametrize("ans", [-1, 3])
def test_is_valid_range_steering_rejects_out_of_range(ans, capsys):
    assert assembly.is_valid_range(3, ans) is False
    assert "ERROR" in capsys.readouterr().out


@pytest.mark.parametrize(
    "ans, expected_message",
    [
        (assembly.GM, "GM"),
        (assembly.TOYOTA, "TOYOTA"),
        (assembly.WIA, "WIA"),
        (4, "고장난 엔진"),
    ],
)
def test_select_engine_sets_q1_and_prints_message(ans, expected_message, capsys):
    assembly.select_engine(ans)

    assert assembly.q1 == ans
    assert expected_message in capsys.readouterr().out


@pytest.mark.parametrize(
    "ans, expected_message",
    [
        (assembly.MANDO, "MANDO"),
        (assembly.CONTINENTAL, "CONTINENTAL"),
        (assembly.BOSCH_B, "BOSCH"),
    ],
)
def test_select_brake_sets_q2_and_prints_message(ans, expected_message, capsys):
    assembly.select_brake(ans)

    assert assembly.q2 == ans
    assert expected_message in capsys.readouterr().out


@pytest.mark.parametrize(
    "ans, expected_message",
    [
        (assembly.BOSCH_S, "BOSCH"),
        (assembly.MOBIS, "MOBIS"),
    ],
)
def test_select_steering_sets_q3_and_prints_message(ans, expected_message, capsys):
    assembly.select_steering(ans)

    assert assembly.q3 == ans
    assert expected_message in capsys.readouterr().out
