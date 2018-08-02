houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def recursive_deliver(houses):
    if len(houses) == 1:
        house = houses[0]
        print("Delivering to {}".format(house))
    else:
        midpoint = len(houses) // 2
        left_side = houses[:midpoint]
        right_side = houses[midpoint:]
        recursive_deliver(left_side)
        recursive_deliver(right_side)

recursive_deliver(houses)
