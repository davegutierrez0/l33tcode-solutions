import random

class RandomizedSet:

    def __init__(self):
        self.randomized_set = []
        self.hash_map = {}

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.randomized_set)
        self.randomized_set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        
        last_element = self.randomized_set[-1]
        index_to_remove = self.hash_map[val]
        self.randomized_set[index_to_remove] = last_element
        self.hash_map[last_element] = index_to_remove
        self.randomized_set.pop()
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        return self.randomized_set[random.randrange(len(self.randomized_set))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()