from permutation import permutation


def combination(cards, r):
    per = permutation(cards, r)
    sor = list(map(sorted, per))
    return list(set(map(tuple, sor)))

def combinations(arr: list, r: int=None):
    r = r if r else len(arr)
    def _backtrack(curr, remain):
        if len(curr) == r:
            yield tuple(curr)
        for i, v in enumerate(remain):
            yield from _backtrack(curr+[v], remain[i+1:])
    yield from _backtrack([], arr)

def combinations_with_replacement(arr: list, r: int=None):
    r = r if r else len(arr)
    def _backtrack(curr, remain):
        if len(curr) == r:
            yield tuple(curr)
        for i, v in enumerate(remain):
            if len(curr) < r:
                yield from _backtrack(curr+[v], remain[i:])
    yield from _backtrack([], arr)



if __name__ == "__main__":
    print(combination([1, 2, 3, 4, 5], 5))