'''

설명

Tuple은 원소의 순서, 크기, 값 모두 변할 수 없는 객체입니다.

함수의 이름을 concat으로 하고, 2개의 인자를 입력받아 2개의 Tuple을 하나로 합쳐 반환하는 함수를 정의하세요.


입력 설명

2개의 Tuple이 concat 함수의 인자로 입력됩니다.


출력 설명

2개의 Tuple을 합쳐 하나의 Tuple을 반환해야 합니다. (Tuple이어야 합니다.)

순서대로 A, B가 입력된다면 A, B가 순서대로 결합되어야 합니다.

'''

def concat(arg1, arg2):
    return tuple(list(arg1) + list(arg2))