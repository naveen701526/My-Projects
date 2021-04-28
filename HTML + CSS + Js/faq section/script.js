const btn = document.querySelectorAll('.faq-toggle')

let btns

btn.forEach(button => {

    button.addEventListener('click', () => {
        let i = 0
        btns = Array.prototype.slice.call(button.parentNode.classList);

        
           
            while (i < btn.length) {
                btn[i].parentNode.classList.remove('active')
                i++
            }
        
        
            // console.log(btns);
        if (btns[1] !== 'active') {
                
            button.parentNode.classList.toggle('active')
            // console.log(button.parentNode);
        }
        // else {
            
        //     // console.log(button.parentNode);
        // }
        
        


        // console.log(button.parentNode.classList);

        
        // console.log(btns);

        // console.log(btns);

        // while (bt) {
            
        // }



        

        

        // console.log(button.parentNode.classList);

        // console.log(button);
    })
})



