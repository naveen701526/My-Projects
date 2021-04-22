const boxes = document.querySelectorAll('.box')


window.addEventListener('scroll', checkBoxes)


checkBoxes()

function checkBoxes() {
    console.log(window.innerHeight);
}