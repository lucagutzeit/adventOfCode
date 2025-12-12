class Range:
    def __init__(self, x: int, y : int):
        if x > y:
            temp = y
            y = x
            x = temp
        
        self.start = x
        self.end = y

    def contains(self, num: int):
        return self.start <= num <= self.end

    def __lt__(self, obj):
        return self.start < obj.start

class Ranges:
    ranges: list[Range] = []

    def add(self, range: Range):
        # If empty list or new range starts after the last one ends
        if not (len(self.ranges) > 0 and range.start <= self.ranges[-1].end):
            self.ranges.append(range)
            return

        # New range ends before first starts
        i = len(self.ranges)
    
        for i, r in enumerate(self.ranges):
            if range.end < r.start:
                self.ranges.insert(i, range)
                return
            # new range inside of existing range
            elif r.contains(range.start) and r.contains(range.end):
                return
            # new range starts before but ends inside
            elif not r.contains(range.start) and r.contains(range.end):
                r.start = range.start
                return
            # new range starts inside but ends after
            elif r.contains(range.start) and not r.contains(range.end): 
                r.end = range.end
                break
            # New range contains range
            elif range.start < r.start and range.end > r.start:
                r.start = range.start
                r.end = range.end
                break
        
        # Handle overlap of later ranges
        while i+1 < len(self.ranges) and self.ranges[i].end >= self.ranges[i+1].start:
            self.ranges[i].end = self.ranges[i+1].end
            self.ranges.pop(i+1)


    def inAny(self, num: int):
        for range in self.ranges:
            if range.contains(num):
                return True
        return False
    
    def getSize(self):
        size = 0
        for range in self.ranges:
            size += (range.end - range.start) + 1
            
        return size

    def checkIntegrity(self):
        for i, range in enumerate(self.ranges[:-1]):
            if range.end < self.ranges[i+1].end:
                continue
            return False
        return True


if __name__ == "__main__":
    count = 0
    ranges = Ranges()
    with open("2025\\day5\\input.txt", "r") as file:
        for line in file:
            if line =="\n":
                break
            
            x, y = line.split("-")
            ranges.add(Range(int(x), int(y)))
        assert ranges.checkIntegrity()

        for line in file:
            line = line.strip()
            food = int(line)
            if ranges.inAny(food):
                count += 1
    
    print(count)
    print(ranges.getSize())