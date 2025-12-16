corners: list[tuple[int, int]] = []
squares: list[tuple[int, int, int]] = []

with open("2025\\day9\\input.txt", "r") as file:
    for line in file:
        line = line.strip()
        x, y = line.split(",")
        corners.append((int(x), int(y)))

for i in range(len(corners)):
    for j in range(i+1):
        sideA = abs((corners[i][0] - corners[j][0])) + 1
        sideB = abs((corners[i][1] - corners[j][1])) + 1
        squares.append((i, j, sideA * sideB))

squares = sorted(squares, key=lambda s: s[2], reverse=True)
print(squares)
print(squares[0][2])

