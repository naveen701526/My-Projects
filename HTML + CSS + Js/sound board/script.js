const sounds = [
    'blank',
    'fade',
    'invincible',
    'myheart',
    'onandon',
    'spectre'
]

sounds.forEach(sound => {
    const btn = document.createElement('button')
    btn.classList.add('btn')


    btn.innerText = sound

    btn.addEventListener('click', () => {
        
        pauseSongs()

        document.getElementById(sound).play()

    })

    document.querySelector('#buttons').appendChild(btn)
})


