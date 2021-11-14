function createQueue(){
    return []
}

function pushToqueue(queue,value){
    return queue.push(value)
}

function popFromQueue(queue,value){
    if(!isQueueEmpty(queue)){
        queue.shift()
    }
}

function peekQueue(queue){
    return queue[0]
}

function isQueueEmpty(queue){
    return queue.length === 0
}

const queue1 = createQueue()
pushToqueue(queue1,'1')
pushToqueue(queue1,'2')
pushToqueue(queue1,'3')
pushToqueue(queue1,'4')
popFromQueue(queue1)
popFromQueue(queue1)
popFromQueue(queue1)
popFromQueue(queue1)

console.log(queue1,isQueueEmpty(queue1),peekQueue(queue1))