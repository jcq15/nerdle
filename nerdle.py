import fractions as fr

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=']
operators = ['+', '-', '*', '/']
words = []

# 逆运算
inv = {
    '+': '-',
    '-': '+',
    '*': '/',
    '/': '*',
}

# 等号只有三个位置

### 等号后面有三位数，只能是加或乘
# xx?x=xxx 或 x?xx=xxx，加或乘可利用交换律
# 将其反过来就是xxx?x=xx和xxx?xx=x
for i in range(10, 100):
    for j in range(0, 10):
        for k in ['+', '*']:
            result = eval(f'{i}{k}{j}')
            if 100 <= result < 1000:
                words.append(f'{i}{k}{j}={result}')
                words.append(f'{j}{k}{i}={result}')
                words.append(f'{result}{inv[k]}{i}={j}')
                words.append(f'{result}{inv[k]}{j}={i}')
print(len(words))
#print(words)

### 等号后面两位数，有这两种：x?x?x=xx, xx?xx=xx, 
# x?xxx=xx 是没有的，xxx?x=xx已经在上面考虑过
# 8/3*6=16 这种是可行的，所以需要用fraction

# x?x?x=xx
for i1 in range(0, 10):
    n1 = fr.Fraction(i1, 1)
    for o1 in operators:
        for i2 in range(0, 10):
            n2 = fr.Fraction(i2, 1)
            for o2 in operators:
                for i3 in range(0, 10):
                    n3 = fr.Fraction(i3, 1)
                    try:
                        res = eval(f'{n1}{o1}{n2}{o2}{n3}')
                        if res.denominator == 1 and 10 <= res < 100:
                            words.append(f'{n1}{o1}{n2}{o2}{n3}={res}')
                    except Exception as e:
                        pass
print(len(words))

#xx?xx=xx
# 两位数除以两位数不可能是两位数，所以这里不考虑除法
for n1 in range(10, 100):
    for n2 in range(10, 100):
        for o in ['+', '-', '*']:
            res = eval(f'{n1}{o}{n2}')
            if 10 <= res < 100:
                words.append(f'{n1}{o}{n2}={res}')
print(len(words))


### 等号后面一位数
# x?x?xx=x, x?xx?x=x, xx?x?x=x
for i1 in range(0, 10):
    n1 = fr.Fraction(i1, 1)
    for o1 in operators:
        for i2 in range(0, 10):
            n2 = fr.Fraction(i2, 1)
            for o2 in operators:
                for i3 in range(10, 100):
                    n3 = fr.Fraction(i3, 1)
                    try:
                        res = eval(f'{n1}{o1}{n2}{o2}{n3}')
                        if res.denominator == 1 and 0 <= res < 10:
                            words.append(f'{n1}{o1}{n2}{o2}{n3}={res}')
                    except Exception as e:
                        pass
print(len(words))

for i1 in range(0, 10):
    n1 = fr.Fraction(i1, 1)
    for o1 in operators:
        for i2 in range(10, 100):
            n2 = fr.Fraction(i2, 1)
            for o2 in operators:
                for i3 in range(0, 10):
                    n3 = fr.Fraction(i3, 1)
                    try:
                        res = eval(f'{n1}{o1}{n2}{o2}{n3}')
                        if res.denominator == 1 and 0 <= res < 10:
                            words.append(f'{n1}{o1}{n2}{o2}{n3}={res}')
                    except Exception as e:
                        pass
print(len(words))

for i1 in range(10, 100):
    n1 = fr.Fraction(i1, 1)
    for o1 in operators:
        for i2 in range(0, 10):
            n2 = fr.Fraction(i2, 1)
            for o2 in operators:
                for i3 in range(0, 10):
                    n3 = fr.Fraction(i3, 1)
                    try:
                        res = eval(f'{n1}{o1}{n2}{o2}{n3}')
                        if res.denominator == 1 and 0 <= res < 10:
                            words.append(f'{n1}{o1}{n2}{o2}{n3}={res}')
                    except Exception as e:
                        pass
print(len(words))

# xxxx?x=x，x?xxxx=x，这只能是xxxx*0=0，穷举四位数即可
for i in range(1000, 10000):
    words.append(f'{i}*0=0')
    words.append(f'0*{i}=0')
print(len(words))

# xxx?xx=x 前面弄过
# xx?xxx=x 不存在这种情况

with open('word_list.txt', 'w') as f:
    for word in words:
        f.write(f'{word}\n')