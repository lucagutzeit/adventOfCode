def turn(start, direction, amount):
    amount = amount % 100

    if direction == "L":
        amount = 100 - amount

    pos = (start + amount) % 100

    if pos == 0:
        return (pos, 1)
    
    return (pos, 0)

def turn2(start, direction, amount):
    count = int(amount / 100)
    amount = amount % 100

    if direction == "L":
        pos = start - amount
    else:
        pos = start + amount

    if 0 < pos < 100:
        return (pos, count)

    # Moved left from 0
    if pos < 0 and start == 0:
        return (pos%100, count)
    
    # Moved over 0 from left or right
    return (pos%100, count+1)
    

count = 0
pos = 50
with open("2025\day1\input.txt", "r") as file:
    for line in file:
        line = line.strip()
        pos, i = turn2(pos, line[0], int(line[1:]))
        count = count + i
        print ("Moved by " + line + " to position " + str(pos) + ". Touched " + str(i) + " times")
        
print(count)