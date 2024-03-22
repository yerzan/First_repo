import random

def get_numbers_ticket(min_val, max_val, quantity):
    if not (1 <= min_val <= max_val <= 1000 and quantity > 0):
        return []
    
    numbers_set = set()

    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_val,max_val))

    numbers_list = sorted(numbers_set)
    return numbers_list

lottery_numbers = get_numbers_ticket(1, 49, 6)
print('Ваші лотерейні білети', lottery_numbers)