from typing import List, Tuple
from combination import combination

def combination_with_replacement(elements: list, r: int=None) -> List[Tuple]:
    if r is None:
        r = len(elements)

    if r == 0:
        return [()]

    combinations = combination(elements, r)
    result = []

    for comb in combinations:
        length = len(comb)
        counter = [0 for _ in range(r)]
        for i in range(length**r):
            for counter_idx in range(len(counter)):
                if counter[counter_idx] >= length:
                    counter[counter_idx] = 0
                    counter[counter_idx + 1] += 1
            result.append(tuple(comb[i] for i in counter))
            counter[0] += 1
        result = list(sorted(set(result)))
    return result

if __name__ == "__main__":
    elements = [".left", ".right"]
    r = 0
    solve = combination_with_replacement(elements, r)
    print(solve)
    print(len(solve))