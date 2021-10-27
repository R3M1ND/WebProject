#Dictionary การเก็บรูปแบบเป็น key กับ value
'''
mydict = {
    'name' : "khim",
    'number' : 63010295
}
mydict = {} <- clear
print(mydict['number'])
print(mydict.get('123',-1)) #get -> เอาไว้ใช้เช็คว่าตัว value เรามีในลิสต์แล้วยัง ถ้าไม่มีจะออกมาเป็น -1 
print(mydict.values()) #ออก value ทั้งหมด 
for i in mydict.values() :
    print(i)

#Set
#myset = set() #set แบบ set ว่าง
myset = {1,2,3,5,6,7,8,9}
myset.add('khim')
print(myset)
print(set(myset))

#Function
def myfunc(num,num2) :
    return num+num2

print(myfunc(1,2))

#Class and func
class myclass :
    def __init__(self,num) : #ในคลาสจะมีตัวแปรอะไรบ้างที่เราจะเอามาใช้งาน
        self.num = 15
    def add(self,num2) :
        return self.num+num2 

x = myclass(15)
print(x.add(1))

txt = "Hello Ja"
new = ""

for i in txt :
    if not i in new :
        new += i
print(i)

g = "FFFFFDCBAAA"
num = int(input())
print(g[num//10])
'''
myinput = int(input())
for i in range(myinput) :   
    for j in range(i+1) :
        print("*",end="")
        j+=1
    print()
    i+=1