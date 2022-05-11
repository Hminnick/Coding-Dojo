function printOdds() {
    for (var i = 1; i < 20; i+=2) {
        console.log(i);
        }
    }

function decreasing() {
    for (i = 100; i >-1 ; i--){
        if(i % 3 == 0){
            console.log(i);
        }
    }
}

for(var i=4; i>-4; i-=1.5) {
    console.log(i);
}

function sigma() {
    var sum = 0;
    for (i = 1; i <= 100; i++) {
        sum += 1;
    }
}
        console.log(sum);

function factorial() {
    var product = 1;
    for (i = 1; i <= 12; i++) {
        product *= i;
    }
}
        console.log(product);