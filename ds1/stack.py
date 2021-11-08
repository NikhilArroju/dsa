def createStack():
    return []


def pushToStack(stack,value):
    return stack.append(value)


def popFromStack(stack):
    if not isStackEmpty(stack):
        stack.pop()
    else:
        print('stack is empty')
    

def peekStack(stack):
    if not isStackEmpty(stack):
        return stack[-1]
    else:
        print('stack is empty')
    


def isStackEmpty(stack):
    return len(stack) == 0


stack1 = createStack()
# pushToStack(stack1,'1')
# pushToStack(stack1,'1')
# pushToStack(stack1,'1')
# pushToStack(stack1,'1')
popFromStack(stack1)
print(stack1,isStackEmpty(stack1),peekStack(stack1))