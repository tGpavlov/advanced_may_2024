def accommodate_new_pets(hotel_cap, pet_max_weight, *pets_info):
    hotel_info = {}
    pets_accommodated = 0
    is_full = False

    result = []

    for pet_type, pet_weight in pets_info:
        if pets_accommodated == hotel_cap:
            is_full = True
            break

        elif pet_weight <= pet_max_weight:
            pets_accommodated += 1

            if pet_type not in hotel_info:
                hotel_info[pet_type] = []
            hotel_info[pet_type].append(pet_weight)

    if not is_full:
        hotel_cap -= pets_accommodated
        result.append(f"All pets are accommodated! Available capacity: {hotel_cap}.")

    else:
        result.append("You did not manage to accommodate all pets!")

    result.append("Accommodated pets:")

    for pet_type, pet_count in sorted(hotel_info.items()):
        result.append(f"{pet_type}: {len(pet_count)}")

    return '\n'.join(result)


# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
