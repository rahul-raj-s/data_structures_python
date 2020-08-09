class Node:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next


class Stack :
    def __init__(self,size=None):
        self.top = None
        self.size = size
        self.nodes = 0
    def push(self,value):
        if( self.size and self.nodes >=self.size):
            raise Exception('Stack full')
        nodeToAdd = Node(value)
        if(self.top):
            nodeToAdd.next = self.top 
        self.top = nodeToAdd
        self.nodes += 1

    def pop(self):
        if(self.top):
            value = self.top.value
            self.top = self.top.next
            self.nodes -=1
            return value
        raise Exception('stack empty')

#test
s1 = Stack(3)
s1.push(5)
s1.push(4)
s1.push(3)

print(s1.pop())
print(s1.pop())
print(s1.pop())

s1.push(2)
s1.push(1)
s1.push(2)
# s1.push(1)

print(s1.pop())
print(s1.pop())
print(s1.pop())