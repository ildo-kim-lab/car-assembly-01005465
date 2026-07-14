from assembly import SEDAN, SUV, TRUCK, GM, TOYOTA, WIA, MANDO, CONTINENTAL, BOSCH_B, BOSCH_S, MOBIS
import assembly as _assembly

def test_produced_car():
    q0 = _assembly.q0
    q1 = _assembly.q1
    q2 = _assembly.q2
    q3 = _assembly.q3

    if q0 == SEDAN and q2 == CONTINENTAL:
        print("FAIL\nSedan에는 Continental제동장치 사용 불가")
    elif q0 == SUV and q1 == TOYOTA:
        print("FAIL\nSUV에는 TOYOTA엔진 사용 불가")
    elif q0 == TRUCK and q1 == WIA:
        print("FAIL\nTruck에는 WIA엔진 사용 불가")
    elif q0 == TRUCK and q2 == MANDO:
        print("FAIL\nTruck에는 Mando제동장치 사용 불가")
    elif q2 == BOSCH_B and q3 != BOSCH_S:
        print("FAIL\nBosch제동장치에는 Bosch조향장치 이외 사용 불가")
    else:
        print("PASS")
