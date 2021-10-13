const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];

// btn variable will refer to button element 
const btn = document.querySelector("#btn");


// color variable will be referencing h2 element
// which displays the value of the color
const color = document.querySelector(".color");


btn.addEventListener("click", () => {
    // get random number between 0 - 3
    // because array are zero index based
    const randomNumber = getRandomNumber(); // calls the function which generates a random index

    // the below statement will add color value
    // to background of the body
    document.body.style.backgroundColor = colors[randomNumber]

    // this statement helps in displaying the value
    // of the color which is displayed on the background
    color.textContent =  colors[randomNumber]

});


function getRandomNumber() {
    // this function will generate a random value which will be
    // the index of the array colors
  return Math.floor(Math.random() * colors.length);
}