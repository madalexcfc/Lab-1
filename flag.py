def draw_swiss_flag():
    red = "\033[41m"   
    white = "\033[47m" 
    reset = "\033[0m"  
    width = 18
    height = 10

    for i in range(height):
        if i in [4, 5]:
            print(red + " " * ((width - 12) // 2) + white + " " * 12 + red + " " * ((width - 12) // 2) + reset)
        elif i in [2, 3, 6, 7]:
            print(red + " " * ((width - 4) // 2) + white + " " * 4 + red + " " * ((width - 4) // 2) + reset)
        else:
            print(red + " " * width + reset)
    print("\n")


if __name__ == '__main__':
    draw_swiss_flag()
