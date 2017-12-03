def GetCode(x, y): return ((x+y) * (x+y-1))//2 - (y-1)

targetCode = GetCode(3019, 3010)

code = 20151125

for i in range(targetCode-1):
    code = (code * 252533) % 33554393

print(code)