from collections import deque

packages = [int(p) for p in input().split()]
couriers = deque(int(c) for c in input().split())

total_weight_delivered = 0

while couriers and packages:
    curr_package = packages.pop()
    curr_courier = couriers.popleft()

    if curr_package <= curr_courier:
        total_weight_delivered += curr_package

        if curr_package < curr_courier:
            curr_courier -= curr_package * 2

            if curr_courier > 0:
                couriers.append(curr_courier)

    else:
        total_weight_delivered += curr_courier
        packages.append(curr_package - curr_courier)


print(f"Total weight: {total_weight_delivered} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver"
          f" the following packages: {', '.join(str(el) for el in packages)}")

elif not packages:
    print(f"Couriers are still on duty:"
          f" {', '.join(str(el) for el in couriers)} but there are no more packages to deliver.")