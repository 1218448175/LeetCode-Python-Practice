class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices: # 更严谨的判断
            return False
        self.indices[val] = len(self.nums) # 补全 self.
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        # 交换逻辑...
        index = self.indices[val]
        last_val = self.nums[-1]
        
        self.nums[index] = last_val
        self.indices[last_val] = index
        
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()