# class Hungry:
#     def __init__(self, menu: list, hungry_rate: int, person):
#         self.menu = menu
#         self.hungry_rate = hungry_rate
#         self.person = person
# #
#     def __getitem__(self, item):
#         return self.menu[item]
#
#     def __str__(self):
#         return self.menu.__str__()
#
# who_hungry = Hungry(["라면", "피자"], 78, "성우")
# print(who_hungry)

# class Callist:
#     def __init__(self, arr: list[int]):
#         self.arr = arr
#
#     def __add__(self, other):
#         return [x + y for x, y in zip(self.arr, other.arr)]
#
# box1 = Callist([1, 3, 2])
# box2 = Callist([3, 4, 1])
#
# print(type(box1))
# print(box1.arr)
# print(box2.arr)
# print(box1 + box2)

# class Callist:
#     def __init__(self, arr: list[int]):
#         self.arr = arr
#
#     def __add__(self, other):
#         return Callist([x + y for x, y in zip(self.arr, other.arr)])
#
#     def __str__(self):
#         return self.arr.__str__()
#
# box1 = Callist(1)
# box2 = Callist(3)
#
# print(type(box1))
# print(box1.arr)
# print(box2.arr)
# print(box1.__add__(box2))
#
# set()

#한 줄에 공백으로 구분된 입력
#example1 =

#한 줄에 하나씩 여러 줄로 구분된 입력
# n = int(input())
# list_ = [input() for i in range(n)]
# print(list_)

#한 줄에 여러개 씩 여러 줄로 구분된 입력
n = int(input())
lis_t = [list(map(int, input().split())) for _ in range(n)]
print(*lis_t)