def instagram_debug(post_list: list, user_list: list) -> dict:
    result = {}
    user = []
    set_ = set(zip(post_list, list(map(int, user_list))))
    for i in set_:
        user.append(i[0])
        result[i[0]] = user.count(i[0])
    return result

print(instagram_debug(['A', 'A', 'B', 'B', 'B', 'C', 'C'],
                      ['1', '1', '1', '1', '1', '1', '2']))
