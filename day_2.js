// The Fibonacci Sequence 

// [0 1 1 2 3 5 8 13 21] ...
// 0 1 2 3 4 5 6  7   8

function fibonacci(number){
    var fibArray = [0, 1];
    for(var i = 2; i <= number; i++){
        fibArray.push(fibArray[i-1] + fibArray[i-2])
    }
    return fibArray[number];
}

console.log(fibonacci(8));
console.log(fibonacci(4));
console.log(fibonacci(20));
console.log(fibonacci(10));