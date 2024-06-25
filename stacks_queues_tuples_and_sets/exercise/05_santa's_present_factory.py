from collections import deque

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

materials = [int(el) for el in input().split()]
magic_levels = deque(int(el) for el in input().split())

crafted = []

while magic_levels and materials:
    material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)


if {'Doll', 'Wooden train'}.issubset(crafted) or {'Teddy bear', 'Bicycle'}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(el) for el in materials[::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join(str(el) for el in magic_levels)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]