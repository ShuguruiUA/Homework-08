from random import randrange,sample

min=1
max=36
quantity = 6

def get_numbers_ticket(min, max, quantity):
    my_list = list()
    not_repeatable = list()
    if min > 0 and max < 1000 and min < quantity < max:
        while len(my_list) < quantity+max:
           my_list.append(randrange(min,max))
        print(my_list)
        for el in my_list:
            if el not in not_repeatable:
                not_repeatable.append(el)
            else:
                continue
        not_repeatable.sort()
        not_repeatable = sample(not_repeatable,k=quantity)
        print(not_repeatable)
        return not_repeatable
    else:
        print(my_list)
        return my_list

get_numbers_ticket(1,3,3)


