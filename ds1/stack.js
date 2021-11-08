function createStack(){
    return []
}

function pushToStack(stack,value){
    return stack.push(value)
}

function popFromStack(stack,value){
    if(!isStackEmpty(stack)){
        stack.pop()
    }
}

function peekStack(stack){
    return stack[stack.length - 1]
}

function isStackEmpty(stack){
    return stack.length === 0
}

const stack1 = createStack()
// pushToStack(stack1,'1')
// pushToStack(stack1,'1')
// pushToStack(stack1,'1')
// pushToStack(stack1,'1')
popFromStack(stack1)
console.log(stack1,isStackEmpty(stack1),peekStack(stack1))