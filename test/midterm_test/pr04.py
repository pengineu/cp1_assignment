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
    while ps != prime_number(ps):
        result.append(prime_number(ps))
        ps = ps // prime_number(ps)
    result.append(prime_number(ps))
    return result

print(decrypt(4096
              ))