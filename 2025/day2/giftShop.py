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
        for i in range(1, len(idStr)//2 + 1):
            part = idStr[:i]
            if len(idStr) % len(part) != 0:
                continue
            div = len(idStr) // len(part)
            if  part * div == idStr:
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