#終極密碼
#產生一個隨機整數先不要印出來1~100
#讓使用者重複去猜
#猜對的話印出答對了
#猜錯的話要告訴他比答案大或比答案小
import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1 #count = count + 1
    k = input('請從1-100猜中一個數字:')
    k = int(k)
    if k == r:
        print('正確答案!!')
        print('你總共猜了', count,'次')
        break
    elif k > r:
        print('比答案大')
    elif k < r:
        print('比答案小')
    print('這是你猜的第', count,'次')