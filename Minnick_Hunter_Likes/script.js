var likes = [9, 12, 9];
var p = [
    document.querySelector("#numberOfLikes1"),
    document.querySelector("#numberOfLikes2"),
    document.querySelector("#numberOfLikes3")
];

function like(id) {
    likes[id]++;
    p[id].innerText = likes[id] + " like(s)";
    console.log(p[id].innerText);
}
