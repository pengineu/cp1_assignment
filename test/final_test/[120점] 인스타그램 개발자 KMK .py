def instagram_debug(post_list: list, user_list: list) -> dict:
    result = dict()
    set_ = set(zip(post_list, user_list))
    for i in set_:
        if i[0] in result:
            result[i[0]] = result[i[0]] + 1
        else:
            result[i[0]] = 1
    return result

print(instagram_debug(['A', 'A', 'B', 'B', 'B', 'C', 'C'],
                      ['1', '1', '1', '1', '1', '1', '2']))