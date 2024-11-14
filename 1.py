def count_in(income: str, search: str):
    s = set(list(search))
    for string in s:
        if string in income:
            yield 1


n = int(input())
love_colors = input()
countries = [input().split() for _ in range(n)]
raiting = list(map(lambda x: [sum(x[0]), x[1], x[2]] if len(x[0]) > 0 else [x[0], x[1], x[2]],[[list(count_in(love_colors, _[1])), len(_[1]), k] for k, _ in enumerate(countries)]))
print(' '.join(map(lambda y: countries[y[2]][0], sorted(sorted(raiting, key=lambda x: x[0]), key=lambda x: x[1]))))
