# Phase 2: 자동차에 들어갈 부품 선택

## 목표

자동차 조립 단계로, Phase 1에서 선택한 차량 타입에 장착할 부품인 엔진, 제동장치, 조향장치를 순서대로 선택한다.

## 입력

각 단계에서 아래 중 하나를 숫자로 입력한다. `0`을 입력하면 이전 단계로 되돌아간다.

| 단계 | 항목 | 입력 | 부품 |
|---|---|---|---|
| step 1 | 엔진 | 1 / 2 / 3 / 4 | GM / TOYOTA / WIA / 고장난 엔진 |
| step 2 | 제동장치 | 1 / 2 / 3 | MANDO / CONTINENTAL / BOSCH |
| step 3 | 조향장치 | 1 / 2 | BOSCH / MOBIS |

## 처리

- `assembly.py`의 `main()` `step == 1~3` 분기에서 순차적으로 입력을 받는다.
- 각 단계마다 `is_valid_range(step, ans)`로 입력 범위를 검증한다.
- 단계별로 `select_engine()`, `select_brake()`, `select_steering()`을 호출하여 선택 결과를 전역 변수 `q1`(엔진), `q2`(제동장치), `q3`(조향장치)에 저장하고 안내 메시지를 출력한다.
- 각 선택 후 다음 단계로 진행하며, 조향장치까지 선택을 마치면 `step`이 4로 진행되어 Phase 3(완성된 차량 테스트)로 이동한다.
- `0` 입력 시 `step`을 1 감소시켜 이전 단계(또는 Phase 1)로 되돌아간다.

## 출력

- 선택한 부품 안내 메시지 (예: "GM 엔진을 선택하셨습니다.")
- 범위를 벗어난 입력의 경우 에러 메시지 출력 후 동일 단계 재시도

## 관련 코드

- `assembly.py`: `show_menu(1~3)`, `is_valid_range()`, `select_engine()`, `select_brake()`, `select_steering()`
