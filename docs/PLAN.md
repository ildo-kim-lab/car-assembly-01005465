# PLAN: 자동차 조립 3단계 구성

`docs/PRD.md`에 정의된 4단계 제조 순서를 아래 3개의 Phase로 묶어서 정리한다. 각 Phase의 상세 내용은 `docs/design/phase1.md`, `docs/design/phase2.md`, `docs/design/phase3.md`를 참고한다.

## Phase 1: 자동차 타입 선택

- 사용자가 Sedan, SUV, Truck 중 차량 타입을 선택한다.
- 관련 코드: `assembly.py`의 `main()` `step == 0` 분기, `select_car_type()`
- 선택 결과는 전역 변수 `q0`에 저장된다.

## Phase 2: 자동차에 들어갈 부품 선택

- 엔진, 제동장치, 조향장치를 순서대로 선택한다.
- 관련 코드: `assembly.py`의 `main()` `step == 1~3` 분기, `select_engine()`, `select_brake()`, `select_steering()`
- 선택 결과는 각각 전역 변수 `q1`(엔진), `q2`(제동장치), `q3`(조향장치)에 저장된다.
- 각 단계는 `0` 입력으로 이전 단계로 돌아갈 수 있다.

## Phase 3: 완성된 차량 테스트

- 1~2단계에서 선택한 부품 조합으로 완성된 차량을 RUN(실제 동작) 또는 Test(호환성 검증)한다.
- 관련 코드: `assembly.py`의 `main()` `step == 4` 분기
  - RUN: `run_produced_car()` — `is_valid_check()`로 호환성 검증 후 동작 여부 출력, 엔진 고장 여부 별도 확인
  - Test: `test_assembly.py`의 `test_produced_car()` — 호환성 규칙별 PASS/FAIL 출력
- 호환성 규칙은 `docs/PRD.md`의 "조립 호환성 규칙" 항목을 따른다.
