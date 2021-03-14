// Given an array of integers, find the next greater element for every element in the array. The next greater element of an element x is the first grater number to the right of x, if there is no such number consider it -1

function findNextGreaterNumber(arr) {
    result = [];
    for (let i = 0; i < arr.length; i++) {
        nextGreaterNumber = -1;
        for (let j = i+1; j < arr.length; j++) {
            if (arr[j] > arr[i]) {
                nextGreaterNumber = arr[j];
                break;
            }
        }
        result.push(nextGreaterNumber)
    }
    return result
}
console.log(findNextGreaterNumber([2, 7, 3, 5, 4, 6, 8]))

