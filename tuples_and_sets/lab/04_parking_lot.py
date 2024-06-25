num = int(input())

parking_lot = set()

for _ in range(num):
    command, car_number = input().split(', ')
    if command == 'IN':
        parking_lot.add(car_number)
    elif command == 'OUT':
        if car_number in parking_lot:
            parking_lot.remove(car_number)


if not parking_lot:
    print('Parking Lot is Empty')
else:
    print(*parking_lot, sep='\n')
