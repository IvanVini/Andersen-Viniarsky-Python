print(
    'Вводите числа массива, нажимая Enter после каждого. При вводе не числового значения программа остановиться и '
    'выдаст все элементы массива кратные 3.')
try:
    arr = []
    while True:
        arr.append(int(input()))
except:
    i = len(arr)
for x in range(0, i):
    if (arr[x] % 3) == 0 and arr[x] > 0:
        print(f'Елемент массива номер {str(x + 1)}, цифра =', + arr[x])
        x += 1
    else:
        x += 1
input('Нажми Enter для выхода...')