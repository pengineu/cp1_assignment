# def timo(G: float, J: float, N:float):
#     room = 1
#     while G != 0:
#         room += 6 * (G - 1)
#         G -= 1
#     efficiency = J * N
#     return room <= efficiency

def timo(G: float, J: float, N: float) -> bool:
    room = 1
    while G != 1:
        room += 6 * (G - 1)
        G -= 1
    return J * N >= room

print(timo(3.0,
7.0,
1.0))