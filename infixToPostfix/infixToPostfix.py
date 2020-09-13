import stack
def getPostfix(infix:str):
    order ={'*':1,'/':1,'+':2,'-':2}
    infix = ''.join(infix.split())
    postfix =''

    for i in infix:
        if(i == '('):
            pass
        elif(i in order):
            pass
        elif(i == ')'):
            pass
        else:
            postfix += i
