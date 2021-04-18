
const progress = document.querySelector('#progress')

const prev = document.querySelector('#prev')
const next = document.querySelector('#next')
const circles = document.querySelectorAll('.circle')


let currentActive = 1


next.addEventListener('click', () => {
    currentActive++
    console.log(currentActive);
    if(currentActive > circles.length) {
        currentActive = circles.length
    }

    update()
})


prev.addEventListener('click', () => {
    currentActive--

    if(currentActive < 1) {
        currentActive = 1
    }

    update()
})


function update() {
    circles.forEach((circle, idx) => {
        if (idx < currentActive) {
            circle.classList.add('active')
        } else {
            circle.classList.remove('active')
        }
    })
    
    const actives = document.querySelectorAll('.active')
    
    progress.style.width = (actives.length - 1) / (circles.length - 1) * 100 + '%'



}