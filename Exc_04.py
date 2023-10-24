from random import randrange,randint


def get_numbers_ticket(min, max, quantity):
    my_list = list()
    if min >= 1 and max <= 1000 and min < quantity < max:
        for num in quantity:
           my_list.append(randint(min,max))
