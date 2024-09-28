s = [float(x) for x in open('C:/Users/PC/Desktop/test/sequence.txt')]
a = [x for x in s if -3<=x<=3]
need = (len(a)/len(s))*100
ost = 100-need
print(f"\u001b[47m{' ' * 50}\u001b[0m")
print(f"\u001b[47m{' ' * 50}\u001b[0m")
print(f"\u001b[47m{' ' * 50}\u001b[0m")
print(f"\u001b[47m{' ' * 29}\u001b[40m{' ' * 4}\u001b[47m{' ' * 17}\u001b[0m")
print(f"\u001b[47m{' ' * 29}\u001b[40m{' ' * 4}\u001b[47m{' ' * 17}\u001b[0m")
print(f"\u001b[47m{' ' * 29}\u001b[40m{' ' * 4}\u001b[47m{' ' * 17}\u001b[0m")
print(f"\u001b[47m{' ' * 29}\u001b[40m{' ' * 4}\u001b[47m{' ' * 17}\u001b[0m")
print(f"\u001b[47m{' ' * 15}\u001b[40m{' ' * 4}\u001b[47m{' ' * 10}\u001b[40m{' ' * 4}\u001b[47m{' ' * 17}\u001b[0m")
print(f"\u001b[47m{' ' * 15}\u001b[40m{' ' * 4}\u001b[47m{' ' * 10}\u001b[40m{' ' * 4}\u001b[47m{' ' * 17}\u001b[0m")
print(f"\u001b[47m{' ' * 15}\u001b[40m{' ' * 4}\u001b[47m{' ' * 10}\u001b[40m{' ' * 4}\u001b[47m{' ' * 17}\u001b[0m")
print(' '*11,'-3<=x<=3',' '*5, 'остальные')
print(' ' * 13, need,'%',' ' * 7, ost,'%')