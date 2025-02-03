class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):

    def update(self, keys, values):

        for item in zip(keys, values):
            self.items_list.append(item)

m = Mapping([1, 2, 3])
print(m.items_list)

ms = MappingSubclass([4, 5, 7])
print(m.items_list)

ms.update(["b", "a"], [7, 8])
print(ms.items_list)
