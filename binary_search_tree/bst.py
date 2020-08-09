class Node:
    def __init__(self,value=0,right=None,left=None,):
        self.right = right
        self.left = left
        self.value = value

class BST:
    def __init__(self,arr =[]):
        self.root = None
    def _addNode(self,value):
        nodeToAdd = Node(value)
        print("Inserting ",value,end="->")
        if(not self.root):
            self.root = nodeToAdd
            print("Root")
            return
        currentNode = self.root
        while(currentNode):
            if(currentNode.value ==  value):
                raise Exception('Trying to add duplicate value')
            if(value < currentNode.value ):
                if(not currentNode.left):
                    print(currentNode.value,"Left")
                    currentNode.left = nodeToAdd
                    break
                else:
                    currentNode = currentNode.left
            elif(value > currentNode.value):
                if(not currentNode.right):
                    print(currentNode.value,"Right")
                    currentNode.right = nodeToAdd
                    break
                else:
                    currentNode = currentNode.right
    def addNode(self,value):
        if(isinstance(value,list)):
            for i in value:
                self._addNode(i)
        else:
            self._addNode(value)
    def _traverse(self,currentNode,type,callback):
        if(currentNode):
            if(type=="PrO"):
                callback(currentNode.value)
            self._traverse(currentNode.left,type,callback)
            if(type=="IO"):
                callback(currentNode.value)
            self._traverse(currentNode.right,type,callback)   
            if(type=="PO"):
                callback(currentNode.value)   
    def traverse(self,type="IO",callback= lambda x:print(x,end="->")):
        self._traverse(self.root,type,callback)
        print('')
    def search(self,key):
        currentNode = self.root
        while(currentNode):
            print(currentNode.value)
            if(currentNode.value == key):
                return True
            elif(currentNode.value>key):
                currentNode = currentNode.left
            elif(currentNode.value<key):
                currentNode = currentNode.right
        return False

    def _countChild(self,node):
        count = 0
        if(isinstance(node,Node)):
            if(node.left):
                count+=1
            if(node.right):
                count += 1
        return count

    def delete(self,value):
        currentNode = self.root
        parent = self.root
        while(currentNode):
            if(currentNode.value == value):
                break
            elif(currentNode.value > value):
                parent = currentNode
                currentNode = currentNode.left
            elif(currentNode.value < value):
                parent = currentNode
                currentNode = currentNode.right
        if(not currentNode):
            return  False
        no_child = self._countChild(currentNode)
        if(no_child==0):
            if(parent.left and parent.left.value == currentNode.value):
                parent.left = None
            else:
                parent.right = None
        elif(no_child == 1):
            if(parent.left and parent.left.value == currentNode.value):
                if(currentNode.left):
                    parent.left = currentNode.left
                else:
                    parent.left = currentNode.right
            else:
                if(currentNode.left):
                    parent.right = currentNode.left
                else:
                    parent.right = currentNode.right
        elif(no_child == 2):
            successor = currentNode.left
            successorParent = None
            while(successor and successor.right):
                if(successor.right):
                    successorParent = successor
                    successor = successor.right
                    
                else:
                    break
            currentNode.value = successor.value
            if(successorParent):
                successorParent.right = None
            else:
                currentNode.left = successor.left
        return True



            


arr =[]
b1 = BST()
b1.addNode([4,2,1,3,5,0])
b1.traverse()
b1.delete(0)
b1.traverse(callback=lambda x : arr.append(x))
print(arr)
b1.traverse('IO')
b1.traverse('PO')
b1.traverse('PrO')
b1.traverse()