# Phase 3: 완성된 차량 테스트

## 목표

Phase 1, 2에서 선택한 부품 조합(`q0`~`q3`)으로 완성된 차량을 실제로 동작(RUN)시키거나 호환성을 검증(Test)한다.

## 입력

| 입력 | 동작 |
|---|---|
| 0 | 처음 화면(Phase 1)으로 돌아가기 |
| 1 | RUN — 조립된 차량 실제 동작 |
| 2 | Test — 조립 유효성 검증 |

## 처리

### RUN (`run_produced_car()`, `assembly.py`)

1. `is_valid_check()`로 부품 조합의 호환성을 검사한다. 호환되지 않으면 "자동차가 동작되지 않습니다" 출력 후 종료한다.
2. 엔진이 "고장난 엔진"(`q1 == 4`)이면 "엔진이 고장나있습니다. 자동차가 움직이지 않습니다." 출력 후 종료한다.
3. 위 조건을 모두 통과하면 선택된 차량 타입, 엔진, 제동장치, 조향장치를 출력하고 "자동차가 동작됩니다."를 출력한다.

### Test (`test_produced_car()`, `test_assembly.py`)

- `assembly` 모듈의 전역 상태(`q0`~`q3`)를 읽어 호환성 규칙을 검사하고, 위반된 규칙이 있으면 해당 사유와 함께 "FAIL"을 출력하고, 없으면 "PASS"를 출력한다.
- 순환 임포트를 피하기 위해 `assembly.py`의 `main()`에서 이 함수를 호출 시점에 지연 임포트한다.

## 호환성 규칙

`docs/PRD.md`의 "조립 호환성 규칙" 5가지를 따른다. 동일한 규칙이 `is_valid_check()`(RUN용)와 `test_produced_car()`(Test용) 두 곳에 중복 구현되어 있으므로, 규칙 변경 시 두 함수를 함께 수정해야 한다.

## 관련 코드

- `assembly.py`: `show_menu(4)`, `is_valid_range()`, `run_produced_car()`, `is_valid_check()`
- `test_assembly.py`: `test_produced_car()`
