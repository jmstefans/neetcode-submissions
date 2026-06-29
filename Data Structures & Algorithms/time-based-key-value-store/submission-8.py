class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)    # hashmap of tuples. key is key like alice, value is tuple like alice, 1. Maybe use 
                                            # a stack b/c we just are interested in the most recent, previous timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        # if the earliest timestamp for this key is greater than the requested timestamp to get then no point in searching
        if self.timemap[key][0][1] > timestamp:
            return ""
        
        # get the key's stack of tuples, binary search it for the most recent, previous timestamp
        l, r = 0, len(self.timemap[key]) - 1
        result = ""
        
        while l <= r:
            m = (l + r) // 2

            if timestamp < self.timemap[key][m][1]:
                r = m - 1

            elif timestamp > self.timemap[key][m][1]:
                l = m + 1
                result = self.timemap[key][m][0]

            else:
                return self.timemap[key][m][0]

        # we know an answer exists and we ended the loop at one element to the left of the real answer
        return result