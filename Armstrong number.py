#Wap to check wheather number is armstrong or not
num = int(input("Enter a number: "))
s = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** s
   temp //= 10
if(num == sum):
    print("armstrong")
else:
    print("not armstrong")
