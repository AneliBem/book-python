words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

users = {"Hans": "active", "Eleonore": "inactive", "Jack": "active"}


for user, status in users.copy().items(): # копіювання та попарне додавання юзер, статус
    if status == "inactive": # виділення неактивних юзерів
        del users[user] # видалення цих юзерів

active_users = {} # створення нового словника
for user, status in users.items():
    if status == "active":
        active_users[user] = status # додавання до нового словника

print(active_users)