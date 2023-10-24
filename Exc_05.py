import random

participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}
#quantity = 2
# keys_list = list(participants.keys())
# print(type(keys_list))
# print(keys_list)
# random.shuffle(keys_list)
# print(keys_list)
# print(random.sample(keys_list, k=quantity))

def get_random_winners(quantity, participants):
    winner_list = list()
    if quantity > len(participants):
        return winner_list
    winner_list = list(participants.keys())
    random.shuffle(winner_list)
    return random.sample(winner_list,k=quantity)

print(get_random_winners(3, participants))