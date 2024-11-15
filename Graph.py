def function():
    max_x = 18
    max_y = 6
    for y in range(max_y, -1, -1):
        line = ""
        for x in range(max_x + 1):
            if y == round(x / 3):
                line += '\x1b[48;5;27;1m \x1b[0m' 
            else:
                line += " "
        print(line)

if __name__ == '__main__':
    function()
