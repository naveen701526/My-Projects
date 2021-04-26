const btn = document.querySelector('#btn')

const quotes = document.querySelector('.quotes')

generateQuote()



function generateQuote() {
    fetch('http://quotes.stormconsultancy.co.uk/random.json')
  .then(response => response.json())
  .then(data => console.log(data));
}