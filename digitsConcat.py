def digitCount(val):
    ret = 1
    while(val>0):
        remainder = val%10
        ret = ret*10
        val = val//10
#         print('remainder=',remainder,'ret=',ret,'val',val)
    return ret
l=[1,21,3,4,5]
num = 0
for i in l:
    num = num*digitCount(i) + i
print(num)
# print(digitCount(21))
