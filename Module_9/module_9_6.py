def all_variants(text: str):
    for part_len in range(1, len(text) + 1):
        # part_len - длина последовательности
        x = 0
        while x + part_len <= len(text):
            yield text[x: x + part_len]
            if part_len == 1:
                x += 1
            else:
                x += part_len - 1


a = all_variants('abc')
for i in a:
    print(i)
