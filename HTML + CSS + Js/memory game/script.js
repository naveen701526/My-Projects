document.addEventListener('DOMContentLoaded', () => {
    // cards which will get displayed
    const cardArray = [
        {
            name: 'fries',
            img: 'images/fries.png',
        },
        {
            name: 'cheeseburger',
            img: 'images/cheeseburger.png',
        },
        {
            name: 'ice-cream',
            img: 'images/ice-cream.png',
        },
        {
            name: 'pizza',
            img: 'images/pizza.png',
        },
        {
            name: 'milkshake',
            img: 'images/milkshake.png',
        },
        {
            name: 'hotdog',
            img: 'images/hotdog.png',
        },
        {
            name: 'fries',
            img: 'images/fries.png',
        },
        {
            name: 'cheeseburger',
            img: 'images/cheeseburger.png',
        },
        {
            name: 'ice-cream',
            img: 'images/ice-cream.png',
        },
        {
            name: 'pizza',
            img: 'images/pizza.png',
        },
        {
            name: 'milkshake',
            img: 'images/milkshake.png',
        },
        {
            name: 'hotdog',
            img: 'images/hotdog.png',
        },
    ];

    const grid = document.querySelector('.grid');
    let cardsChosen = [];
    let cardsChosenId = [];
    let cardsWon = [];

    // function which will create the board when the page is loaded

    function createBoard() {
        for (let i = 0; i < cardArray.length; i++) {
            const card = document.createElement('img');
            card.setAttribute('src', 'images/blank.png');
            card.setAttribute('data-id', i);
            card.addEventListener('click', flipCard);
            grid.appendChild(card);
        }
    }

    // this function will decide whether the two cards choosen are same or not... main logic of game

    // a function which will flip the cards when the user clicks on it.
    function flipCard() {
        let cardId = this.getAttribute('data-id');
        cardsChosen.push(cardArray[cardId].name);
        cardsChosenId.push(cardId);
        this.setAttribute('src', cardArray[cardId].img);
        // if (cardsChosen.length === 2) {
        //     setTimeout(checkForMatch, 500);
        // }
    }

    createBoard();
});
