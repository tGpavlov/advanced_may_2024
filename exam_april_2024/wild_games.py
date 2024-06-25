def draw_cards(*args, **kwargs):
    monsters = []
    spells = []

    for name, card_type in (list(args) + list(kwargs.items())):
        if card_type == 'monster':
            monsters.append(f"  ***{name}")
        elif card_type == 'spell':
            spells.append(f"  $$${name}")

    if monsters:
        result = "Monster cards:\n" + "\n".join(sorted(monsters, reverse=True))
    if spells:
        result += "\nSpell cards:\n" + "\n".join(sorted(spells))

    # if monsters:
    #     print("Monster cards:")
    #     [print(''.join(el)) for el in monsters]     ...........NEED RETURN FFS
    # if spells:
    #     print("Monster cards:")
    #     [print(''.join(el)) for el in spells]


print(draw_cards(("celtic guardian", "monster"),
                 ("earthquake", "spell"),
                 ("fireball", "spell"),
                 raigeki="spell", destroy="spell", ))
