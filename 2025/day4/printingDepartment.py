mods = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
mods.pop(mods.index((0, 0)))

class diagram():
    diagram: list[list[str]] = []
    rows = 0
    columns = 0
    def addRow(self, row: list[str]):
        if not len(self.diagram) == 0:
            assert len(row) == len(self.diagram[0])
            self.columns = len(row)
        
        self.diagram.append(row)
        self.rows += 1

    def countNeigbours(self, row: int, col: int):
        count = 0

        for x, y in mods:
            vertical = row + x
            horizontal = col + y
            if not (0 <= horizontal < self.columns):
                continue
            if not (0 <= vertical < self.rows):
                continue
            if self.diagram[vertical][horizontal] == "@":
                count += 1
        
        return count
    
    def evaluate(self, loop = False):
        movablePaper = 0
        moved = True
        while moved:
            moved = False
            for row in range(self.rows):
                for col in range(self.columns):
                    if self.diagram[row][col] == ".":
                        continue
                    if self.countNeigbours(row, col) < 4:
                        movablePaper += 1
                        if loop:
                            moved = True
                            self.diagram[row][col] = "."
            if not loop:
                return movablePaper

        return movablePaper

    def getDiagram(self):
        return self.diagram
    

if __name__ == "__main__":
    plan = diagram()
    with open("2025\\day4\\input.txt", "r") as file:
        for line in file:
            line = line.strip()
            plan.addRow(list(line))

    print(plan.evaluate(True))
    

