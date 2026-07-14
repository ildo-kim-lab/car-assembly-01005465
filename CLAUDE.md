# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

콘솔 기반 자동차 조립 시뮬레이터입니다. 사용자가 메뉴에서 부품(차량 타입, 엔진, 제동장치, 조향장치)을 순서대로 선택하면 조합의 호환성을 검증하고, 조립된 차량을 실행(RUN)하거나 검증 결과를 테스트(Test)할 수 있습니다.

## 실행 방법

```bash
python assembly.py
```

대화형 메뉴가 실행되며, 각 단계에서 숫자를 입력해 부품을 선택합니다. `0`은 이전 단계로 돌아가기, `exit`은 종료입니다.

## 테스트 방법

```bash
pytest test_assembly.py
pytest test_assembly.py::test_produced_car   # 단일 테스트만 실행
```

`test_assembly.py`는 `assembly.py`의 검증 로직을 검사하는 테스트 코드입니다. `assembly` 모듈의 전역 상태(`q0`~`q3`, 선택된 부품 값)를 참조하여 현재 선택된 조합이 유효한지 출력합니다.

## 아키텍처

- `assembly.py`: 메인 실행 파일. 메뉴 상태 머신(`main()`), 부품 선택 함수(`select_car_type`, `select_engine`, `select_brake`, `select_steering`), 조립 유효성 검사(`is_valid_check`), 실제 동작(`run_produced_car`)을 포함합니다.
  - 선택된 부품은 전역 변수 `q0`(차량 타입), `q1`(엔진), `q2`(제동장치), `q3`(조향장치)에 저장됩니다.
  - 메뉴는 `step` 값(0~4)으로 진행되는 상태 머신 구조입니다: 0=차량 타입, 1=엔진, 2=제동장치, 3=조향장치, 4=완료(RUN/Test 선택).
  - `main()`의 Test 메뉴(`step == 4`, `ans == 2`)는 순환 임포트를 피하기 위해 `test_assembly.test_produced_car`를 함수 내부에서 지연 임포트(lazy import)합니다.
- `test_assembly.py`: `assembly.py`로부터 부품 상수를 임포트하고, `assembly` 모듈을 `_assembly`로 임포트하여 전역 상태(`q0`~`q3`)를 읽어 검증 결과(PASS/FAIL)를 출력하는 `test_produced_car()`를 정의합니다.

### 부품 종류 (상수)

| 항목 | 상수 | 값 |
|---|---|---|
| 차량 타입 | `SEDAN`, `SUV`, `TRUCK` | 1, 2, 3 |
| 엔진 | `GM`, `TOYOTA`, `WIA` | 1, 2, 3 (4는 "고장난 엔진") |
| 제동장치 | `MANDO`, `CONTINENTAL`, `BOSCH_B` | 1, 2, 3 |
| 조향장치 | `BOSCH_S`, `MOBIS` | 1, 2 |

### 호환성 규칙 (`is_valid_check` / `test_produced_car`에 중복 구현됨)

- Sedan + Continental 제동장치 → 불가
- SUV + TOYOTA 엔진 → 불가
- Truck + WIA 엔진 → 불가
- Truck + Mando 제동장치 → 불가
- Bosch 제동장치 + Bosch 조향장치가 아닌 조향장치 → 불가
- 엔진이 "고장난 엔진"(값 4)인 경우 `run_produced_car()`는 별도로 처리하며 차량이 움직이지 않습니다.

이 호환성 규칙은 `assembly.is_valid_check()`와 `test_assembly.test_produced_car()` 두 곳에 동일한 로직이 중복되어 있으므로, 규칙을 수정할 때는 두 파일을 함께 갱신해야 합니다.
