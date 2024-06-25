def team_lineup(*info):
    football_info = {}

    result = []

    for player_name, country in info:

        if country not in football_info:
            football_info[country] = []
        football_info[country].append(player_name)

    sorted_football_info = sorted(football_info.items(), key=lambda x: (-len(x[1]), x[0]))

    for country, names in sorted_football_info:

        result.append(f"{country}:")

        for name in names:
            result.append(f"  -{name}")

    return '\n'.join(result)


print(team_lineup(
    ("Lionel Messi", "Argentina"),
    ("Neymar", "Brazil"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Harry Kane", "England"),
    ("Kylian Mbappe", "France"),
    ("Raheem Sterling", "England")))
