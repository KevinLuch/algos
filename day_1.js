// Balance Point
// Write a function that returns whether the given array has a balance point between indices
// where one side's sum is equal to the other's
// ex: given [1,1,1,1] > return true, because between indices 0 and 1 the sum of rthe left and right are eqaul 

function balance(arr){
    var left = 0
    var right = 0

    for(i=0; i<arr.length; i++){
        right += arr[i]
    }

    for(j=0; j<arr.length; j++){
        left += arr[j]
        right -= arr[j]
        if(left == right){
            return true
        }
    }
        return false
}

console.log(balance([1,1,1,1]))
console.log(balance([1,1,1]))
