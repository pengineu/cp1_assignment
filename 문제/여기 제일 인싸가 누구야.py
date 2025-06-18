def insider(args: list) -> str:
    li = []
    dic = {}
    for i in args:
        for j in i:
           li.append(j)
           dic[j] = li.count(j)
    di = dict(zip(dic.values(), dic.keys()))
    return di[max(di)]

print(insider([ {'Mark', 'Bill'}, {'Mark', 'Kanye', 'Hiddleston'}, {'Mukyeom', 'Dasom', 'Mark'} ]))