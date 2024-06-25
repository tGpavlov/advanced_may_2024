from collections import deque

money = [int(m) for m in input().split()]
food_prices = deque([int(p) for p in input().split()])

eaten_food = 0

while money and food_prices:

    curr_money = money.pop()
    curr_price = food_prices.popleft()

    if curr_money == curr_price:
        eaten_food += 1
        continue

    elif curr_money > curr_price:
        eaten_food += 1
        curr_money -= curr_price

        if money:
            curr_money += money.pop()

        money.append(curr_money)

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif eaten_food:
    print(f"Henry ate: {eaten_food} food{'' if eaten_food == 1 else 's'}.")
else:
    print("Henry remained hungry. He will try next weekend again.")
