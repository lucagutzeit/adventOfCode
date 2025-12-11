# Returns the number of neighbor fields increased do more than 3. If change is negative returns 0.
def modifyNeighbors(col, row, adjacency: list[list[int]], change = 1) -> int:
    moreThan3 = 0
    width = len(adjacency[0])
    for horizontal in range(col-1, col+2, 1):
        # Out of bounds check
        if 0 > horizontal or horizontal >= width:
            continue
        for vertical in range(row-1, row+2, 1):
            # Out of bounds check 
            if 0 > vertical:
                continue
            # Not influence itself
            if vertical == row and horizontal == col:
                continue
            # Only increase where it matters
            if adjacency[vertical][horizontal] == -1 or adjacency[vertical][horizontal] >= 4:
                continue
            adjacency[vertical][horizontal] += 1
            if adjacency[vertical][horizontal] > 3:
                moreThan3+=1
    return moreThan3

def getRemovablePapers() -> int:
    moreThan3 = 0
    countPaper = 0
    adjacency: list[list[int]] = []
    with open("2025\\day4\\input.txt", "r") as file:
        width = len(file.readline().strip())
        file.seek(0)
        adjacency.append([0]*width)
        for row, line in enumerate(file):
            line = line.strip()
            # Adding next row preamptivly to enable count. Count will be overwritten if not paperroll. Additional row removed at the end.
            adjacency.append([0]*width)
            for col, char in enumerate(line):
                # Only increase neighbors if field is paperroll
                if char != "@":
                    adjacency[row][col] = -1
                    continue
                # Lookahead to right neighbor to prevent increasing it above 3
                if col < width-1 and line[col+1] != "@":
                    adjacency[row][col+1] = -1
                countPaper += 1
                moreThan3 += modifyNeighbors(col, row, adjacency)
        adjacency.pop()
        return countPaper - moreThan3

if __name__ == "__main__":
    print(f"Removable paperroll: {getRemovablePapers()}")



