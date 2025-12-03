from functools import reduce

def max(list: list[int], start=0, stop=-1):
    idxMax = start
    for i in range(start+1, len(list) + stop):
        if list[i] > list[idxMax]:
            idxMax = i
    return (idxMax, list[idxMax])

def main():
    sum = 0
    with open("2025\\day3\\input.txt", "r") as file:
        for line in file:
            line = line.strip()
            arr = [int(x) for x in line]
            concat = ""
            lastIdx = -1

            for i in range(11, -1, -1):
                if len(arr[lastIdx+1:]) == i+1:
                    concat += str(reduce(lambda x, y: int(str(x) + str(y)), arr[lastIdx+1:]))
                    break
                idx, num = max(arr, lastIdx+1, -i)
                lastIdx = idx
                concat += str(num)

            sum += int(concat)

    print(sum)

if __name__ == "__main__":
    main()