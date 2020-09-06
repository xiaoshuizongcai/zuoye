# a=input("请输入衣服数量")
# b=95
# if int(a)*b>=300:
#     print((int(a)*b*0.85),"元")
# else:
#     print((int(a)*b),"元")        
# zuixiao=10
# a=input("三人一排的余数")
# b=input("五人一排的余数")
# c=input("七人一排的余数")
# answer=False
# while zuixiao<100:
#     zuixiao+=1
#     if zuixiao%3==int(a) and zuixiao%5==int(b) and zuixiao%7==int(c):
#         print(zuixiao)
#         answer=True
# if(!answer):
#     print("无解") 
# a=100
# while a<999:
#     a+=1
#     if ((a%10)**3)+((a//10%10)**3)+((a//100)**3)==a:
#         print(a)
# for i in range(1,6):
#     print(i,end=" ")
#     for j in range(1,i):
#        print(i*(j+1),end=" ")
#     print("")
a=int(input("行数"))
for i in range(1,a+1):
    for j in range(1,2*a):
        if(j<i+1):
            print(j,end="")
        elif(j>2*a-i):
            print(2*a-j,end="")
        else:
            print(i,end="")
    print("")
# for i in range(1,a):
#     for j in range(1,a-i+1):
#         print(j,end="")
#     print("")


