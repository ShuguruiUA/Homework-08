import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

#cats = []#[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats_dict = [{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'}, {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]
cats_list = list()


# print(cats.nickname)
# for i in cats:
#     cats_list.append(dict(i._asdict()))

# print(cats_list)

#for data in cats_dict:
#cats = list(Cat(**val) for val in cats_dict)
cats = namedtuple('Cat', set(k for k in d.keys() for d in cats_dict))

print(cats)

# new_dict = {}

# print(isinstance(Cat, dict))

# print(type(cats))
#print(isinstance(cats, collections))

#def convert_list(cats):