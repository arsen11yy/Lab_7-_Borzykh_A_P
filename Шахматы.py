k = int(input('k: '))
l = int(input('l: '))
m = int(input('m: '))
n = int(input('n: '))

if len([ x for x in [ k, l, m, n ] if x < 1 or x > 8 ]) > 0:
    print('Некорректные значения')
    exit()
    
if (k + l + m + n) % 2 == 0:
    print('а) Поля ({}, {}) и ({}, {}) являются полями одного цвета'.format(k, l, m, n))
else:
    print('а) Поля ({}, {}) и ({}, {}) являются не полями одного цвета'.format(k, l, m, n))

fig = int(input('1. Ферзь\n2. Ладья\n3. Слон\n4. Конь\n>'))

if fig < 1 or fig > 4:
    print('Некорректные значения')
    exit()
    
if ((fig == 1 and (k == m or l == n or k - l == m - n or k + l == m + n)) or
    (fig == 2 and (k == m or l == n)) or
    (fig == 3 and (k - l == m - n or k + l == m + n)) or
    (fig == 4 and ((abs(k - m) == 1 and abs(l - n) == 2) or (abs(k - m) == 2 and abs(l - n) == 1)))):
    print('б) Фигура на ({}, {}) угрожает полю ({}, {})'.format(k, l, m, n))
else:
    print('б) Фигура на ({}, {}) не угрожает полю ({}, {})'.format(k, l, m, n))
    
fig = int(input('1. Ферзь\n2. Ладья\n3. Слон\n>'))

if fig < 1 or fig > 3:
    print('Некорректные значения')
    exit()
    
if ((fig == 1 and (k == m or l == n or k - l == m - n or k + l == m + n)) or
    (fig == 2 and (k == m or l == n)) or
    (fig == 3 and (k - l == m - n or k + l == m + n))):
    print('в) Фигура на ({}, {}) может одним ходом попасть на поле ({}, {})'.format(k, l, m, n))
else:
    print('в) Фигура на ({}, {}) не может одним ходом попасть на поле ({}, {})'.format(k, l, m, n))
    if fig == 1 or fig == 2:
        print('Можно попасть за два хода. Следующий ход: ({}, {})'.format(k, n))
    elif fig == 3:
        if (k + l + m + n) % 2 == 0:
            for p in range(1, 9):
                for q in range(1, 9):
                    if (p == k and q == l) or (p == m and q == n):
                        continue
                    if (k - l == p - q or k + l == p + q) and (p - q == m - n or p + q == m + n):
                        print('Можно попасть за два хода. Следующий ход: ({}, {})'.format(p, q))
                        break
        else:
            print('в) Фигура на ({}, {}) вообще не может попасть на поле ({}, {})'.format(k, l, m, n))
        
input()
