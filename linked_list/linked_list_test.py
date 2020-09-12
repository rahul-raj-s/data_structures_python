from linked_list import SLinkedlist
from random import randint
s1 = SLinkedlist()
#inserting random values in list
for i in range(10):
    s1.add(randint(2,999)) #add value to end
#insert 
s1.add(10) #Insert 10 @ end
s1.add(10,2) # Insert 10 @ position 2
s1.add(10,'start') # Insert 10 @ start

#traverse
s1.traverse() # each value in linked list will be printed

#traverse s1 and map each value to a function
def showValue(value):
    # print(value)
    pass
s1.traverse(showValue) # each nodevalue is send to showValue


#SLinkedlist is iteratable
for i in s1:
    print(i,end="->")
print()

for i in s1(5):  #SLinkedlist is iteratable, s1(max) to limit the number of nodes
    print(i,end="->")
print()

#delete
s1.add(4)   
s1.delete(4) #delete first 4 in list
s1.delete(1,'position') #delete node at position 1

#reverse()
s1.reverse()

#middle()
print(s1.middle()) #print middle element of array

#sort()
s1.traverse()
s1.sort() #sort list in ascending order
s1.sort(order = 'desc') #sort  list in descending order

#remove_duplicates
s2 = SLinkedlist()
s2.add(1)
s2.add(1)
s2.add(2)
s2.add(3)
s2.add(3)
s2.traverse() #1->1->2->3->3
s2.remove_duplicates()
s1.traverse() #1->2->3

# addition of two SLinkedlist():
test1 = SLinkedlist()
test2 = SLinkedlist()
test1.add(1)
test1.add(2)
test1.add(3)
test2.add(4)
test2.add(5)
test2.add(6)
test1.traverse() #1->2->3
test2.traverse() #4->5->6
test1+test2     #append test2 at the end of test1(doesnot affect test2)
test1.traverse() #1->2->3->4->5->6
test2.traverse() #4->5->6