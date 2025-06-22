def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def permutation(cards: list, r: int = 0):
    card = [[cards.pop()]]
    card_repo = []
    while cards:
        new_card = cards.pop()
        for c in card:
            cd_repo = []
            for idx in range(len(c)+1):
                cd = c.copy()
                for _ in range(idx):
                    cd_repo.append(cd.pop())
                cd.append(new_card)
                for _ in range(idx):
                    cd.append(cd_repo.pop())
                card_repo.append(cd)
        card = card_repo
        card_repo = []
    if r:
        card = list(map(lambda x: x[:-r], card))
        card = set(map(tuple, card))
    card = list(card)
    return card

def desire(cards: list) -> int:
    card = permutation(cards)
    cnt = 0
    for c in card:
        str_card_list = list(map(str, c))
        per = int(''.join(str_card_list))
        if isprime(per):
            cnt += 1
    return cnt

print(desire([1, 1]))