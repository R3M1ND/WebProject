'''print("hello",end="+")
print("ja")

x= 10
y=10.5
z="hello"
print(x)
print(z)
print(x+y)
print(str(x)+z) #เอาstring ต่อกับตัวเลข
print(50//2) #หารไม่เอาเศษ
print(10**2) #ยกกำลัง

if 10 > 5 :
    print("hello")
elif 200 > 30 : #else if
    print("ja")
else :
    print("error")

if 20 >= x <= 30 : 
    print("hello")
else :
    ("error")

#------------------Input---------------
a = int(input("Enter number : 150"))
#print(type(a)) เช็คไทป์
print(a+30)

for i in range(10,20,1) : #ตัวแรก start ตัวที่สอง ตัวจบ ตัวสุดท้าย step
    print(i)

for i in range(20) : #ออกถึงตัว stop
    print(i)

x = "hello python"
for i in x : #ปริ้นทีละ index 
    print(i)
for i in range(12) : #เขียนแบบนี้ก็ออกทีละ index แต่จะยาวกว่า แบบด้านบนดีกว่า
    print(x[i])

x = 0
while x < 10 :
    print(x)
    x += 1 #mean x++
else :
    print("end")

x = "11111111"
for i in x :
    x = int(i)

x = 0
x,y = [int(i) for i in input().split()] #ลูปแบบย่อ

hello = "Hello" #บอก index
print(hello[-2])

hello = "Hello" 
print(hello[0 : 5 : 2]) #start at 0 stop at 5 step 2 หรือจะไม่ใส่ตัว step ก็ได้ 
print(hello[ : 5 : ]) #ไม่ใส่ start
'''
x = 10
print(f"hello {x} ja {x}") #จัด format 
print("hello {} ja ".format(x))