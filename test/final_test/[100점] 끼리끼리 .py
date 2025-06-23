import numpy as np

def friend(haesol: float, datas: dict):
    idxlist = []
    for i in datas.values():
        i = np.array(i)
        idxlist.append(abs(np.mean((i - haesol))))
    data = list(datas.keys())
    return data[idxlist.index(min(idxlist))]

print(friend(11.2,

{
    "아날로그파": [-3.7, -1.3, -0.9],
    "디지털파": [4.9, 1.7, 5.3, 3.15],
    "러다이트 운동가들": [-101.5, -209.7, -154.5]
}))