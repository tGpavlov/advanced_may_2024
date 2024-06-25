def boarding_passengers(ship_cap, *pass_info):
    boarding_info = {}
    boarded_pass = 0
    waiting_pass = sum(el[0] for el in pass_info)
    is_full = False

    result = []

    for guests, benefit_prog in pass_info:
        if guests > ship_cap:
            continue

        if benefit_prog not in boarding_info:
            boarding_info[benefit_prog] = 0
        boarding_info[benefit_prog] += guests

        ship_cap -= guests
        boarded_pass += guests

        if ship_cap <= 0:
            is_full = True
            break

    sorted_boarding_info = sorted(boarding_info.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    result.append("Boarding details by benefit plan:")

    for program, guests_num in sorted_boarding_info:
        result.append(f"## {program}: {guests_num} guests")

    if waiting_pass == boarded_pass:
        result.append("All passengers are successfully boarded!")

    if waiting_pass > boarded_pass and is_full:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")

    if waiting_pass > boarded_pass and not is_full:
        result.append(f"Partial boarding completed. Available capacity: {ship_cap}.")

    return '\n'.join(result)


# print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'),
#                           (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
#
#
# print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
#
#
# print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))