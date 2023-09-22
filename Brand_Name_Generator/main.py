import random

adj = ['amused', 'angry', 'annoyed', 'annoying',	'anxious',	'arrogant', 'ashamed',	'attractive',	'average',
'awful', 'bad',	'beautiful']

animals = ['wolf', 'lion', 'tigon', 'liger', 'tiger', 'shark', 'horse',  'cheetah', 'crocodile']

random_adj = random.choice(adj)
random_animals = random.choice(animals)

print(random_adj + " " + random_animals)
