// set initial count
let count = 0;


// select value and buttons
// value variable refers to 
// an element with value as its id
const value = document.querySelector('#value')

// btns variable refers to an element with btn as its class name
const btns = document.querySelectorAll('.btn')


btns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        const styles = e.currentTarget.classList;
        if (styles.contains('decrease')) {
            count--;
        }
        else if (styles.contains('increase')) {
            count++;
        }
        else if (styles.contains('reset')) {
            count = 0
        }
        if (count > 0) {
            value.style.color = 'green'
        }
        else if (count < 0) {
            value.style.color = 'red'
        }
        else if (count === 0) {
            value.style.color = 'grey'
        }
        value.textContent = count
    })
})