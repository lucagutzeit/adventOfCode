import math

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distanceTo(self, box):
        x = pow(box.x-self.x, 2)
        y = pow(box.y-self.y, 2)
        z = pow(box.z-self.z, 2)
        res = math.sqrt(x + y + z)
        return res

class Distance:
    def __init__(self, distance: float, box1, box2):
        self.distance = distance
        self.box1 = box1
        self.box2 = box2

    def getDistance(self):
        return self.distance

class Circuit:

    def __init__(self, boxs: list[Box] = []):
        self.boxs = boxs

    def add(self, box):
        self.boxs.append(box)

    def merge(self, circuit):
        for box in circuit.boxs:
            self.boxs.append(box)
        return self
    
    def size(self):
        return len(self.boxs)

if __name__ == "__main__":
    boxs: list[Box] = []
    circuits: list[Circuit] = []
    distances: list[Distance] = []
    plan: dict[Box, Circuit] = {}


    with open("2025\\day8\\input.txt", "r") as file:
        for line in file:
            line = line.strip()
            x, y, z = line.split(",")
            box = Box(int(x), int(y), int(z))
            boxs.append(box)
            circuit = Circuit([box])
            plan[box] = circuit
            circuits.append(circuit)

    for i in range(len(boxs)):
        for j in range(i+1, len(boxs)):
            distances.append(Distance(boxs[i].distanceTo(boxs[j]), boxs[i], boxs[j]))
    
    distances = sorted(distances, key=lambda distance: distance.distance)
    # print([f"{x.distance}: {x.box1} {x.box2}" for x in distances])

    for distance in distances[:]:        
        circuit1: Circuit = plan[distance.box1]
        circuit2: Circuit = plan[distance.box2]

        if circuit1 == circuit2:
            continue
        
        for box in circuit2.boxs:
            plan[box] = circuit1

        circuit1 = circuit1.merge(circuit2)
        circuits.remove(circuit2)

        if len(circuits) == 1:
            print(f"Box 1 ({distance.box1.x}) * Box 2 ({distance.box2.x})")
            print(f"One circuit: {distance.box1.x * distance.box2.x}")
            break


    circuits = sorted(circuits, key=lambda circuit: circuit.size(), reverse=True)
    print(len(circuits))
    if len(circuits) > 1:
        print(circuits[0].size() * circuits[1].size() * circuits[2].size())