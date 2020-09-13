from stack import Stack
def evaluatePostfix(postfix:str)->float:
    operators = {'*':lambda a,b:a*b,'/':lambda a,b:a/b,'-':lambda a,b:a-b,'+':lambda a,b:a+b}
    s1 = Stack()
    for i in postfix:
        if(i==' '):
            continue
        if(i in operators):
            a = s1.pop()
            b = s1.pop()
            a = float(a)
            b = float(b)
            s1.push(operators[i](b,a))
        else:
            s1.push(i)
    temp = float(s1.pop())
    if(not s1.isEmpty()):
        raise Exception('Invalid expression')
    if(int(temp)-temp==0):
        return int(temp)
    return temp
# print(evaluatePostfix('3 5 * 6 2 / + 4 -'))

