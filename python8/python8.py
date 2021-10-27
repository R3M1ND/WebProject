#stack
''''''
class stack :
    def __init__(self) : #ประก่าดตัวแปรไว้ใช้ในคลาส 
        self.data = []
    def __str__(self) :
        return str(self.data) #return ค่าในลิสต์ออกมา 
    def is_empty(self) :
        return len(self.data) == 0
    def __len__(self) :
        return len(self.data)  #ขนาดของค่าที่อยู่ในสแต็กว่ามีกี่อัน เป็นการตรวจ 
    def push(self,e) :
        self.data.append(e) #ใส่ข้อมูลไปหลังสุดในลิสต์
    def pop(self) : #เอาค่าออก 
        if self.is_empty() :
            return "empty"
        return self.data.pop() #เอาตัวหลังสุดออกไป 
    def peek(self) : #ดูตัวสุดท้าย ว่าใส่อะไรไป
        if self.is_empty() :
            return "empty"
        return self.data[-1] #เอาตัวล่างสุด 0 = ตัวแรกสุด

s = stack()
print(s.is_empty())
s.push(123)
s.push(789)
s.push(456)

print(len(s))
#print(s)
#s.pop()  
#s.pop()
#s.pop()
#print(s.pop())
print(s)
print(s.peek())


'''
#Queue
class queue :
    def __init__(self) :
        self.data = []
    def __str__(self) :
        return str(self.data)
    def empty(self) :
        return len(self.data) == 0
    def enq(self,d) :
        self.data.append(d)
    def deq(self) :
        if self.empty() :
            return "Q is Empty"
        return self.data.pop(0)  #เอาตัวแรกออก 
    def size(self) : #บอกขนาด
        return len(self.data)
    def first(self) : #ดูตัวแรก 
        return self.data[0]

q = queue()
q.enq(123)
q.enq(456)
#print(q.empty())
#print(q.deq())
#print(q.empty())
print(q)
print(q.size())
print(q.first())


class Nodes :
    def __init__(self,data = None,next = None) :
        self.data = data
        self.next = next
class linkedlist :
    '''