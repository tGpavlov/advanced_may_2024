def grocery_store(**products):
    products = sorted(products.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    return '\n'.join(f"{p}: {q}" for p, q in products)

    # result = []
    #
    # for product, quantity in products:
    #     result.append(f"{product}: {quantity}")
    #
    # return '\n'.join(result)



print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
