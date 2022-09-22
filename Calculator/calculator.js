let display = document.getElementById('screen');

let buttons = Array.from(document.getElementsByTagName('button'));

buttons.map(button => {
    button.addEventListener('click', (e) => {
        switch(e.target.innerText){
            case 'AC':
                display.innerText = '';
                break;
            case '√':
                display.innerText = Math.sqrt(display.innerText);
                break;
            case 'x^2':
                display.innerText = Math.pow(display.innerText, 2);
                break;
            case 'DEL':
                if (display.innerText) {
                    display.innerText = display.innerText.slice(0, -1);
                }
                break;
            case '=':
                try{
                    display.innerText = eval(display.innerText); //NOTE: NEVER USE EVAL TO AVOID MALICIOUS CODE
                } catch {
                    display.innerText = 'Error!'
                }
                break;
            default:
                display.innerText += e.target.innerText;
        } 
    })
})