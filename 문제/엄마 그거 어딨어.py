import collections

def find_socks(words: str):
    result = []
    if "Socks" in words:
        words_deque = collections.deque(words.split())
        for i in range(len(words_deque)):
            next_word = words_deque.popleft()
            if next_word != "Socks":
                result.append(next_word)
    return ' '.join(["Socks"] + result)

print(find_socks("Book Bag Shoes Meal Socks Glasses"))