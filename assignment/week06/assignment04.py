'''

설명

Norm2란 집합 원소들을 제곱하고 나서 모두 더한 후 제곱근을 계산하는 함수이며, 다음 식을 따릅니다.

image.png



함수의 이름을 norm으로 하고, 인자로 List가 주어질 때 Norm2 값을 반환하는 함수를 정의하세요.

sum 함수는 사용할 수 없습니다.


입력 설명

List 타입으로 1개의 인자가 주어집니다. List의 길이는 0 이상입니다.

List의 원소는 모두 실수입니다.

e.g. [a, b, ...]


출력 설명

Norm2 함수의 결과값을 반환해야 합니다.

소수점 3번째 자리에서 반올림하여 소수점 2번째 자리까지 사용합니다.

만약 결과가 정수일 경우 첫번째 자리까지 사용합니다.

e.g. 2.0


'''

def norm(arg):
    square = map(lambda x: x**2, arg)
    su_m = 0
    for i in square:
        su_m += i

    result = su_m ** 0.5
    return round(result, 2)