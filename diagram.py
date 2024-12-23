def sequence(filename="sequence.txt"):
    with open("C:/Users/PC/Desktop/test/Lab-1/sequence.txt") as sequence:
        data = [float(line) for line in sequence]
    correct = [x for x in data if -3 <= x <= 3]
    ratio = int((len(correct) / len(data)) * 100)      
    diff = 100 - ratio
    blue = "\u001b[44m"
    reset = "\u001b[0m"
    width = 20
    height = 10

    for i in range(height):
        if i < min(height - ratio // 10, height - diff // 10):
            print(" " * width + reset)
        elif i < max(height - ratio // 10, height - diff // 10):
            print(" " * 12 + blue + " " * 2 + reset)
        else:
            print(" " * 5 + blue + " " * 2 + reset + " " * 5\
                   + blue + " " * 2 + reset)
    print("corr(30%)" + " " * 1 + "diff(70%)")
    
    
if __name__ == '__main__':
    sequence()
