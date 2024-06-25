num_of_guests = int(input())

guest_list = set()

for _ in range(num_of_guests):
    guest_list.add(input())

reservation_number = input()

while reservation_number != 'END':
    if reservation_number in guest_list:
        guest_list.remove(reservation_number)
    reservation_number = input()

print(len(guest_list), *sorted(guest_list), sep='\n')
