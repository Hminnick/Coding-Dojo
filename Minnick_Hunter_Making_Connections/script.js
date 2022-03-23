console.log("page loaded...");

var username = document.querySelector("#username");
var request1 = document.querySelector("#request1");
var request2 = document.querySelector("#request2");
var two = document.querySelector("#two");
var fivehundred = document.querySelector("#five-hundred");

function edit() {
    username.innerText = "any other name";
}

function accept(id) {
    console.log("accept");
    var element = document.querySelector(id);
    element.remove();
    two.innerText--;
    fivehundred.innerText++;
}

function remove(id) {
    console.log("remove");
    var element = document.querySelector(id);
    element.remove();
    two.innerText--;
}