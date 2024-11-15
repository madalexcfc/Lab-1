def draw_pattern_j():
    blue = "\u001b[44m"
    reset = "\u001b[0m"
    width = 21
    height = 7
    
    for i in range(height):
        if i == 0 or i == (height - 1):
            print(reset + " " * ((width - 17) // 2) + blue + " " * 7 + reset + " " * 3 + blue + " " * 7 + reset)
        elif i == 1 or i == (height - 2):
            print(reset + " " * ((width - 19) // 2) + blue + " " + reset + " " * 7 + blue + " " + reset + " " + blue + " " + reset + " " * 7 + blue + " " + reset)
        else:
            print(blue + " " + reset + " " * 9 + blue + " " + reset + " " * 9 + blue + " " + reset)
    print("\n")


draw_pattern_j()