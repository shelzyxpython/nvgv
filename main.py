#word = input('Введите слово:')
#print(word[2])
#print(word[-2])
#print(word[0:5])
#print(word[0:-2])
#print(word[0:-1:2])
#print(word[1::2])
#print(word[::-1])
#print(word[::-2])
#print(len(word))

#words = input()
#print(words.count(' ') + 1)

#word = input()
#rule = len(word) // 2
#print(word[:rule], word[rule:])

#word = input()
#quantity = word.find('f')
#quantity_2 = word.rfind('f')
#if quantity == -1 and quantity_2 == -1:
#    print('ничего')
#elif quantity >= 0 and quantity_2 >= 0:
#    print(quantity, quantity_2)
#elif quantity >= 0 and quantity_2 == -1:
#    print(quantity)
#elif quantity == -1 and quantity_2 >= 0:
#    print(quantity_2)

#word = input()
#word_1 = word.find('h')
#word_2 = word.rfind('h')
#word_3 = word[:word_1] + word[word_2+1:]
#print(word_3)

#word = input()
#print(word.replace('1','one'))

#word = input()
#print(word.replace('@', ''))

#word = input()
#word_1 = word.find('h')
#word_2 = word.rfind('h')
#print(word[:word_1 + 1] + word[word_1 + 1:word_2 - 1].replace('h','H') + word[word_2 - 1:])

#условия

#number_1 = int(input());number_2 = int(input()) #a,b = int(input()), int(input())
#print(number_1 if number_1 < number_2 else print(number_2)) #print(min(a,b))

#x = int(input())
#if x > 0:
#    print(1)
#elif x < 0:
#    print(-1)
#else:
#    print(0)

#column = int(input()) # столбик
#wrap = int(input()) # ряд
#color = column % 2 == wrap % 2
#if color:
#    print('YES')
#else:
#    print('NO')

#year = int(input())
#if year % 4 == 0 and year % 100 != 1 or year % 400 == 0:
#    print('YES')
#else:
#    print('NO')

#fst = int(input())
#snd = int(input())
#trd = int(input())
#if fst == snd == trd:
#    print(3)
#elif fst == snd:
#    print(2)
#elif fst == trd:
#    print(2)
#elif snd == trd:
#    print(2)
#else:
#    print(0)

#a_1 = int(input())
#a_2 = int(input())
#b_1 = int(input())
#b_2 = int(input())
#if a_1 == b_1 or a_2 == b_2:
#    print('YES')
#else:
#    print('NO')

#n = int(input())
#m = int(input())
#k = int(input())
#if (k % n == 0 or k % m == 0) and k < n * m:
#    print('YES')
#else:
#    print('NO')

#n,m,x,y = int(input()),int(input()),int(input()),int(input())
#if n > m:
#    n, m = m, n
#if x >= n / 2:
#    x = n - x
#if y >= m / 2:
#    y = m - y
#if x < y:
#    print(x)
#else:
#    print(y)