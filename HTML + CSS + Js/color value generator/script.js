const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];


const btn = document.querySelector("#btn");

const color = document.querySelector(".color");


btn.addEventListener("click", () => {
    // get random number between 0 - 3
    // because array are zero index based
    const randomNumber = getRandomNumber();
    document.body.style.backgroundColor = colors[randomNumber]
    color.textContent =  colors[randomNumber]
//   document.body.style.backgroundColor = colors[randomNumber];
//   color.textContent = colors[randomNumber];
});


function getRandomNumber() {
  return Math.floor(Math.random() * colors.length);
}