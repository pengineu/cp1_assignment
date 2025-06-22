def permutation(cards: list, r: int):
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

    card = list(map(lambda x: x[:-r], card))
    card = set(map(tuple, card))
    card = list(card)
    return card

print(permutation([1, 2, 3, 4, 5], 2))


def combination(cards, r):
    per = permutation(cards, r)
    sor = list(map(sorted, per))
    return list(set(map(tuple, sor)))


print(combination([1, 2, 3, 4, 5], 2))