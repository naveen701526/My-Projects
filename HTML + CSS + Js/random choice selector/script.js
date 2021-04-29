// tagsEl refers to div tag with id tags where we'll 
// be adding our tags for the game
const tagsEl = document.getElementById('tags')

// textarea points to Element where we'll enter the choices
const textarea = document.getElementById('textarea')


// when page is loaded automatically it'll point on textarea element
textarea.focus()



// input section where we start our game flow starts from here
textarea.addEventListener('keyup', e => {
    createTags(e.target.value)

    if (e.key === 'Enter') {
        setTimeout(() => {
            e.target.value = ''
        }, 10)

        randomSelect()

    }

})




// when input is entered with comma separator
// it creates a tag for every input with separator
function createTags(input) {
    const tags = input.split(',').filter(tag => tag.trim() !== '').map(tag => tag.trim())

    tagsEl.innerHTML = ''

     tags.forEach(tag => {
        const tagEl = document.createElement('span')
        tagEl.classList.add('tag')
        tagEl.innerText = tag
        tagsEl.appendChild(tagEl)
    })
}




// after entering of choice in textarea element
// this function will start the game and give us the result
function randomSelect() {
    const times = 30

    const interval = setInterval(() => {
        const randomTag = pickRandomTag()

        highlightTag(randomTag)

        setTimeout(() => {
            unHighlightTag(randomTag)
        }, 100)
    }, 100);

    setTimeout(() => {
        clearInterval(interval)

        setTimeout(() => {
            const randomTag = pickRandomTag()

            highlightTag(randomTag)
        }, 100)

    }, times * 100)
}




// this function gives you a random nodelist Element
// each time it is called
function pickRandomTag() {
    const tags = document.querySelectorAll('.tag')
    return tags[Math.floor(Math.random() * tags.length)]
}



// function which add highlight class on span element
// when it is selected
function highlightTag(tag) {
    tag.classList.add('highlight')
}




// function which removes highlight class on span element
// when it is not selected
function unHighlightTag(tag) {
    tag.classList.remove('highlight')
}