const squares = document.querySelectorAll('.square');

const mole = document.querySelector('.mole');

const timeLeft = document.querySelector('#time-left');

const score = document.querySelector('#score');

let result = 0;
let hitPosition;
let timerId = null;

function randomSquare() {
    squares.forEach((square) => {
        square.classList.remove('mole');
    });

    let randomSquare = squares[Math.floor(Math.random() * 9)];

    randomSquare.classList.add('mole');
}

setInterval(randomSquare, 500);
