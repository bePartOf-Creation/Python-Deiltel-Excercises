import random

articles: list = ["the", "a", "one", "some", "any"]
nouns: list = ["boy", "girl", "dog", "town", "car"]
verbs: list = ["drove", "jumped", "ran", "walked", "skipped"]
preposition: list = ["to", "from", "over", "under", "on"]

for _ in range(20):
    sentence = "{} {} {} {} {} {}. ".format(
        random.choice(articles),
        random.choice(nouns),
        random.choice(verbs),
        random.choice(preposition),
        random.choice(articles),
        random.choice(nouns),
    ).capitalize()
    print(sentence)