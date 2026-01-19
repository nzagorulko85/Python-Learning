# TODO решите задачу
import json

file = "input.json"


def task() -> float:
    with open(file) as f:
        data = json.load(f)
    total = 0
    for d in data:
        total += d["score"] * d["weight"]
    return round(total, 3)


print(task())
