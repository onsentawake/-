'''
Lのリストに完全数
Mのリストにほぼ完全数が入っている。（完全数の約数＋１で完全数になる数）
forで千回回して、jに代入。
もしi％ｊ＝＝0ならば、ｋとｊを足しなさい。
kがiに等しくなったら、Lに加えなさい。
'''


L=[]
for i in range(1,1001):
    k=0
    for j in range(1,i):
        if (i%j==0):
            k+=j
    if i==k:
        L.append(i)
        
M=[]
for i in range(1,1001):
    k=0
    for j in range(1,i):
        if (i%j==0):
            k+=j
    if i==(k+1) or i ==(k=1):
        M.append(i)
    


input_line = int(input())
for i in range(input_line):
    a = 0
    num = int(input())
    if num in L:
        print(f'{num}は完全数です。')
    elif num in M:
        print(f'{num}は完全数ではありませんが、近い数字です。')
    else:
        print('ちゃうねん')
    a += 1
