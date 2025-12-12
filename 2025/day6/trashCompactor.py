import re

reOperands = re.compile("([*+]\s*)\1*")


class Calculation:
    def __init__(self, operand: str, size: int):
        self.operand = operand
        self.size = size
        self.nums: list[str] = []
        if operand == "*":
            self.result = 1
        elif operand == "+":
            self.result = 0
        else:
            raise TypeError()
        
    def add(self, num: str):
        self.nums.append(num)
    
    def cephalopodCalc(self):
        rotated = []
        for i in range(self.size):
            rotated.append(int("".join([num[i] for num in self.nums])))
        
        print(rotated)
        
        return self.calc(rotated)

    
    def humanCalc(self) -> int:
        return self.calc([int(x) for x in self.nums])
         
    def calc(self, nums: list[int]):
        result = 1 if self.operand == "*" else 0
        for num in nums:
            if self.operand == "*":
                result *= num
            elif self.operand == "+":
                result += num
            else:
                raise TypeError()
        return result
        
    def getResult(self):
        return self.result
    
    
def fromOperandsLine(line: str) -> list[Calculation]:
    matchs = reOperands.findall(line)
    calculations = [Calculation(match[0], len(match)-1) for match in matchs[:-1]]
    calculations.append(Calculation(matchs[-1][0], len(matchs[-1])))
    return calculations

def take(obj: Calculation, line: str) -> tuple[str, str]:
    out = line[:obj.size]
    line = line[obj.size+1:]

    return (line, out)

if __name__ == "__main__":
    input: list[Calculation] = []
    lines = []
    with open("2025\\day6\\input.txt", "r") as file:
        lines = [line for line in file]

    calculations = fromOperandsLine(lines.pop())
    for line in lines:
        for calc in calculations:
            line, num = take(calc, line)
            calc.add(num)

    simpleSum: int = 0
    cepahlodSum: int = 0
    for c in calculations:
        simpleSum += c.humanCalc()
        cepahlodSum += c.cephalopodCalc()

    print(simpleSum)
    print(cepahlodSum)