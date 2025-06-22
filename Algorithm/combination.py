from permutation import permutation


def combination(cards, r):
    per = permutation(cards, r)
    sor = list(map(sorted, per))
    return list(set(map(tuple, sor)))

if __name__ == "__main__":
    print(combination([1, 2, 3, 4, 5], 2))