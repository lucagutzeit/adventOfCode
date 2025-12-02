import re
def simpleInvalid(start, end):
    sum = 0
    for id in range(int(start), int(end)+1):
        idStr = str(id)
        if len(idStr) % 2 == 1:
            continue
        
        middle = int(len(idStr)/2)
        left = idStr[:middle]
        right = idStr[middle:]

        if left == right:
            sum += id
    return sum

def complexInvalid(start, end):
    sum = 0
    for id in range(int(start), int(end)+1):
        idStr = str(id)
        for i in range(1, len(idStr)):
            part = idStr[:i]
            pattern = re.compile(part)
            found = pattern.findall(idStr)
            if len(found) * len(part) == len(idStr):
                sum += id
                break

    return sum

simpleSum = 0
complexSum = 0
with open("2025\\day2\\input.txt", "r") as file:
    ranges = file.read().split(",")
    for r in ranges:
        start, end = r.split("-")
        simpleSum += simpleInvalid(start, end)
        complexSum += complexInvalid(start, end)


print("Summe: " + str(complexSum))