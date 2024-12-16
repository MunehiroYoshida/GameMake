import random
a=random.randint(1,15)
b=random.randint(1,15)
print("車"*a+"東"+"車"*b)
num=int(input("東は、左から何番目にありますか？"))
if num==a+1:
        print("正解！")
else:
    print("間違い",a+1,"番目です。")
    
