x = ''

while len(x) < 5:
    y = input('Vvod Dannih: ')
    if y == 'o':
        continue
    if y == 'l':
        break
    x += y

else:
    print(x)

print('Programma prodoljaet rabotu')