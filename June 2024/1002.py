def commonChars(words: list[str]) -> list[str]:
    maps = []
    for word in words:
        temp = {}
        for char in word:
            if char not in temp:
                temp[char] = 1
            else:
                temp[char] += 1
            maps.append(temp)
    first_map = maps.pop()
    for count in first_map:
        for other_map in maps:
            if count not in other_map:
                first_map[count] = 0
            else:
                first_map[count] = min(first_map[count], other_map[count])
    out_lst = []
    for count in first_map:
        for i in range(first_map[count]):
            out_lst.append(count)
    return out_lst
