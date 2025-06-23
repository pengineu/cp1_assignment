# def decrypt(ps):
#     result = []
#     repo = []
#     for i in range(2, ps + 1):
#         if ps % i == 0:
#             result.append(i)
#             ps = ps // i
#             break
#
#     while repo != result:
#         repo = result.copy()
#         for i in range(2, ps + 1):
#             if ps % i == 0:
#                 result.append(i)
#                 ps = ps // i
#                 break
#     return result

def prime_number(num):
    for div in range(2, num+1):
        if div == num:
            return div
        elif num % div == 0:
            return div

def decrypt(ps):
    result = []
    password = prime_number(ps)
    while ps != password:
        result.append(password)
        ps = ps // password
        password = prime_number(ps)
    result.append(password)
    return result

if __name__ == "__main__":
    test_case = [
        1372,
        2310,
        4096
    ]

    result = [
        [2, 2, 7, 7, 7],
        [2, 3, 5, 7, 11],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ]
    for t, r in zip(test_case, result):
        if decrypt(t) != r:
            print(False)
        else:
            print(True)