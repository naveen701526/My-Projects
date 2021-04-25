const sounds = [
    'blank',
    'fade',
    'invincible',
    'myheart',
    'onandon',
    'spectre',
]

const stops = document.querySelector('#but')
const resets = document.querySelector('#but1')

sounds.forEach(sound => {
    const btn = document.createElement('button')
    btn.classList.add('btn')


    btn.innerText = sound

    btn.addEventListener('click', () => {
        
        // pauseSongs()
        sounds.forEach(sound => {
        song = document.getElementById(sound)
        song.pause()
        
    })

        stops.addEventListener('click', (e) => {
    document.getElementById(sound).pause()
})
        resets.addEventListener('click', (e) => {
            document.getElementById(sound).pause()
            document.getElementById(sound).currentTime = 0
            
})
    
        
    
        document.getElementById(sound).play()
        
        

    })
    

    

   
    






    document.querySelector('#buttons').appendChild(btn)


     
})





    
    

