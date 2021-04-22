const images = document.querySelectorAll('img')
const lightbox = document.getElementById('lightbox')

images.forEach(image => {
    image.addEventListener('click', e => {
        lightbox.classList.add('active')
        const img = document.createElement('img')
        img.src = image.src
        lightbox.appendChild(img)
    })
})