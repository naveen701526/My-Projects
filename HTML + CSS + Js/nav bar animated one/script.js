const nav = document.querySelector('#nav')

const toggle = document.querySelector('#toggle')


toggle.addEventListener('click', () => {
    nav.classList.toggle('active')
})