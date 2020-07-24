class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.next = None

class SLinkedlist:
    def __init__(self):
        self.header = None
        self._length = 0
    def length(self):
        return self._length
    def __isValidPosition__(self,position):
        if(position in ['start','end']):
            return True
        if(position <= self._length and position >=0):
            return True
        raise TypeError("Invalid position")

    # position: 'start','end',index(0 based),default='end'
    # throws Error: when position is not valid
    def addNode(self,val=0,position='end'):
        if(self.__isValidPosition__(position)):
            if(position == 'start'):
                count = 0
            elif(position == 'end'):
                count = self._length
            else:
                count = position
            nodeToAdd = Node(val)
            if(count == 0):
                nodeToAdd.next = self.header
                self.header = nodeToAdd
                self._length += 1
                return
            currentNode = 0
            node = self.header
            while(node.next and currentNode < count-1 ):
                node = node.next
                count += 1
            nodeToAdd.next = node.next
            node.next = nodeToAdd
            self._length += 1
    
    # takes argument a function which is mapped with each value of list.
    # if callOn is not provided then it simply prints the values.
    def traversList(self,callOn=lambda a : print(a,end="->")):
        node = self.header
        while(node):
            if(callOn):
                callOn(node.dataval)
            node = node.next
        print("")

    # search for a value in list(return position(0 based))
    # return -1 for no match
    def search(self,val):
        node = self.header
        count = 0
        while(node):
            if(node.dataval == val):
                return count
            count += 1
            node = node.next
        return -1
    
    # Delete node based on = value || position , default = 'position'
    # Returns True if node deleted else False
    def delete(self,value,on='value'):
        if(on not in ['position','value']):
            raise TypeError('Invalid value of "on"')
        node = self.header
        if(self._length == 0):
            return False
        if(on == 'position' and self.__isValidPosition__(value)):
            if(self._length == 1 ):
                value = header.dataval
                self.header = None
                self._length = 0
                return value
            count = 0
            while(node and count < value-1):
                node = node.next
                count += 1
            node.next = node.next.next
            self._length -= 1
        elif(on == 'value'):
            if(node.dataval == value):
                self.header=None
                self._length -= 1
                return True
            count = 0
            while(node.next):
                if(node.next.dataval == value): 
                    node.next = node.next.next
                    self._length -= 1
                    return True
                node = node.next
                count += 1
            
       
    def reverse(self):
        prev = None
        current = self.header
        next = None
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current= next
        self.header = prev
             
