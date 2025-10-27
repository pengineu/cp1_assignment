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
        card = list(map(lambda x: x[:r], card))
        card = set(map(tuple, card))
    card = list(map(tuple, card))
    return card


def product(arr: list, r: int=None):
    r = r if r else len(arr)
    def _backtrack(curr, remain):
        if len(curr) == r:
            yield tuple(curr)
        for i, v in enumerate(remain):
            if len(curr) < r:
                yield from _backtrack(curr+[v], remain[:i]+remain[i:])
    yield from _backtrack([], arr)


if __name__ == "__main__":
    print(permutation([".left", ".right", ".left"], 2))
