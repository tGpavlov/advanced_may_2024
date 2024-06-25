def cookbook(*info):
    recipes_info = {}
    result = ''

    for recipe_name, cuisine, ingredients in info:

        if cuisine not in recipes_info:
            recipes_info[cuisine] = []
        recipes_info[cuisine].append((recipe_name, ingredients))

    sorted_recipes_info = sorted(recipes_info.items(), key=lambda x: (-len(x[1]), x[0]))

    for cuisine, recipe_name in sorted_recipes_info:
        sorted_recipe_name = sorted(recipe_name, key=lambda x: x[0])

        result += f"{cuisine} cuisine contains {len(recipe_name)} recipes:\n"

        for name, ingredients in sorted_recipe_name:
            result += f"  * {name} -> Ingredients: {', '.join(ingredients)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
