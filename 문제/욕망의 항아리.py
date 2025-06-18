def isprime(n):
    li = list(range(2, n+1))
    while li == [] or li[0] < n:
        li = list(filter(lambda x: x % li[0] != 0, li))
    if li == []:
        return False
    return True

def desire(cards: list) -> int:
    card = [[cards.pop()]]
    d = 2
    card_repo =[]
    while cards:
        new_card = cards.pop()
        for i in card:
            last_one = i.copy()
            last_one.append(new_card)
            card_repo.append(last_one)
            for idx in range(1, len(i) + 1):
                repo = []
                next_last = i.copy()
                for _ in range(idx):
                    repo.append(next_last.pop())
                next_last.append(new_card)
                for _ in range(idx):
                    next_last.append(repo.pop())
                card_repo.append(next_last)
        card = card_repo
        card_repo = []
        d += 1
    cnt = 0
    for c in card:
        str_card_list = list(map(str, c))
        permutation = int(''.join(str_card_list))
        if isprime(permutation):
            cnt += 1
    return cnt


#print(desire([1,2,3,4,5,6,7,8,9]))
print(isprime(117))