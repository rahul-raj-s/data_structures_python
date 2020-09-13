from stack import Stack
import re
def proccessInfix(infix:str):
    processed = []
    infix =''.join(infix.split())
    oprators =('+','-','*','/',')','(')
    lastString = ''
    for i in infix:
        if(i in oprators):
            processed.append(lastString)
            processed.append(i)
            lastString = ''
        else:
            lastString += i
    if(lastString):
        processed.append(lastString)
    return processed

def getPostfix(infix:str):
    order ={'*':2,'/':2,'+':1,'-':1}
    infix = proccessInfix(infix)
    postfix = []
    s1 = Stack()
    for i in infix:
        if(i==' ' or i==''):
            continue
        if(i == '('):
            s1.push('(')
        elif(i == ')'):
            while((not s1.isEmpty()) and (s1.top.value!='(')):
                postfix.append(s1.pop())
            if(s1.isEmpty()):
                raise Exception('Invalid Expression')
            s1.pop()
        elif(i in order):
            if(s1.isEmpty()):
                s1.push(i)
            else:
                while(not s1.isEmpty() and s1.top.value!='(' and (order[s1.top.value]>=order[i])):
                    postfix.append(s1.pop())
                s1.push(i)
        else:
            postfix.append(i)
    while(not s1.isEmpty()):
        postfix.append(s1.pop())
    return postfix
# print(getPostfix('a+b*c'))
# print(getPostfix('(a+b)-c*d'))


