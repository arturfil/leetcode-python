import random
import json

def read_file(file_name):
    file = open(file_name)

    data = json.load(file)

    return data


def get_notdone_problems():
    not_done = [] # problems not done
    data = read_file("data.json")

    for obj in data["problems"]:
        if obj["done"] == False:
            not_done.append(obj)

    return not_done


def choose_random(exclude, category):
    probs = get_notdone_problems()

    if exclude == "True":
        probs = [x for x in probs if x["isFrom75"] == True]

    if category != "all":
        probs = [x for x in probs if x["category"] == category]

    print("not done ->", len(probs))

    idx = random.randint(0, len(probs)-1)

    print("Problem ->", probs[idx]["title"])
