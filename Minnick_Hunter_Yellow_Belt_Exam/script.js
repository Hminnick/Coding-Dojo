function alertLater() {
    alert("The Ninjas have won!")
    console.log("The Ninjas have won!")
}

setTimeout(alertLater, 13000);

var side3 = document.querySelector(".side-3")

function remove() {
    side3.remove() ;
}

var score = [314,159]
var newScore = [
    document.querySelector("#score1"),
    document.querySelector("#score2")
];

function increase(id){
    score[id]++;
    newScore[id].innerText = score[id];
}