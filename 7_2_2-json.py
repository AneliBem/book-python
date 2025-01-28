import json
with open('work.txt', 'r', encoding="utf-8") as f:
    x = [1, 'simple', 'list']
    print(json.dumps(x))
    # json.dump(x, f) # закодування ('w')

    x = json.load(f) # декодування ('r')
    print(x)
