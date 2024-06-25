def even_odd_filter(**kwargs):
    result = {}

    if 'even' in kwargs:
        result['even'] = [el for el in kwargs['even'] if el % 2 == 0]

    if 'odd' in kwargs:
        result['odd'] = [el for el in kwargs['odd'] if el % 2 != 0]

    return dict(sorted(result.items(), key=lambda kvp: -len(kvp)))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
