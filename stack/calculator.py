import sys
from infixToPostfix import getPostfix
from postfixEvaluate import evaluatePostfix

print('CALCULATOR')
while(True):
    x  = input('->')
    if(x =='exit'):
        break
    try:
        x = getPostfix(x)
        x = evaluatePostfix(x)
        print(x)
    except:
        print("Syntax Error")
