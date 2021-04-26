const btn = document.querySelector('#btn')

const quotes = document.querySelector('.quotes')


btn.addEventListener('click', generateQuote)

generateQuote()






function generateQuote() {
    fetch('http://quotes.stormconsultancy.co.uk/random.json')
  .then(response => response.json())
  .then(data => quotes.innerText=data.quote);
}