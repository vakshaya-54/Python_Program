# num=int(input())
# while not (num>=0 and num<=9):
#     sums=0
#     while num!=0:
#         rem=num%10
#         sums=sums+rem
#         num=num//10
#     num=sums
# else:
#     print(num)
#AMSTRONG NUMBER
# num=int(input())
# digits=0
# temp=num
# temp1=num
# while num!=0:
#     digits+=1
#     num//=10
# sums=0
# while temp!=0:
#     rem=temp%10
#     sums=sums+rem**digits
#     temp=temp//10
# if temp1==sums:
#     print("amstrong number")
# else:
#     print("not a amstrong number")