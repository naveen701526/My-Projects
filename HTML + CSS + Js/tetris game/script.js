document.addEventListener('DOMContentLoaded', () => {


    const grid = document.querySelector('.grid')
    let squares = Array.from(document.querySelectorAll('.grid div'))

    const scoreDisplay = document.querySelector('#score')
    
    const startBtn = document.querySelector('#start-button')
    const width = 10
    
      //The Tetrominoes
  const lTetromino = [
    [1, width+1, width*2+1, 2],
    [width, width+1, width+2, width*2+2],
    [1, width+1, width*2+1, width*2],
    [width, width*2, width*2+1, width*2+2]
  ]

})