function alwaysHungry(arr) {
    count = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] = "food") {
            console.log("yummy");
            count++;
        }
    }
    if(foodCount == 0) {
        console.log("I'm Hungry")
    }
}
alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4, 1, 5, 7, 2]);


function highPass(arr, cutoff) {
    var filteredArr = [];
    for(var i = 0; i < arr.length;i++){
        if(arr[i] > cuttoff){
            filteredArr.push(arr[i]);
        }
    }

    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);


function betterThanAverage(arr) {
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        sum = sum + arr[i];
    }
    var avg = sum / arr.length
    var count = 0

    for(i = 0; i <arr.length; i++){
        if(arr[i] > avg) {
            count++
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result);


function reverse(arr) {
    var left = 0;
    var right = arr.length - 1;
    while(left < right) {
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        right --;
        left++;
    }
    return arr;
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);


function fibonacciArray(n) {
    var fibArr = [0, 1];
    while( fibArr.length < n) {
        var previous = fibArr[ fibArr.length-1];
        var otherPrev = fibArr[fibArr.length -2];
        fibArr.push(previous + otherPrev);
    }
    return fibArr;
}
   
var result = fibonacciArray(10);
console.log(result);
