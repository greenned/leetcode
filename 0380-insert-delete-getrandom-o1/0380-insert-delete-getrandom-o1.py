class RandomizedSet:

    def __init__(self):
        self.hash_set = set()
        

    def insert(self, val: int) -> bool:
        if val in self.hash_set:
            return False
        else:
            self.hash_set.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.hash_set:
            self.hash_set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.hash_set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()