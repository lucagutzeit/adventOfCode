if __name__ == "__main__":
    with open("2025\\day7\\input.txt", "r") as file:
        line = file.readline().strip()
        idx = line.find("S")
        length = len(line)
        paths = [0 for i in range(length)]
        paths[idx] = 1

        for line in file:
            line = line.strip()
            for i in range(length):
                if line[i] == "^" and paths[i] > 0:
                    if i > 0:
                        paths[i-1] += paths[i]
                    if i < length -1:
                        paths[i+1] += paths[i]
                    paths[i] = 0
        sum = 0
        for num in paths:
            sum+=num
        print(sum)
                
