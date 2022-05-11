console.log("page loading...");

var btn = document.querySelector(".footer");

function remove() {
    btn.remove();
}

function c2f(temp) {
    return Math.round(9 / 5 * temp + 32);
}

function f2c(temp) {
    return Math.round(5 / 9 * (temp - 32));
}

function convert(element) {
    console.log(element.value);
    for(var i = 1; i < 9; i++) {
        var temp = document.querySelector("#temp" + i)
        var tempvalue = parseInt(temp.innerText);
        if(element.value == "°C") {
            temp.innerText = f2c(tempvalue) + "°";
        } else {
            temp.innerText = c2f(tempvalue) + "°";
        }
    }
}