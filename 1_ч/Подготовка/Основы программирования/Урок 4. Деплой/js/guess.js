alert('Для начала игры нужно ввести хотябы одно имя.\nДля выходы из игры введи выход.')
let player_1 = prompt('Игрок №1, введи своё имя:')
let player_2 = prompt('Игрок №2, введи своё имя:')
let player_1Answer = '';
let player_2Answer = '';
let exit = 'выход'

if(player_1 || player_2){
    while(player_1 || player_2){
        let answer = parseInt(Math.random()*10)
        if(player_1){
            player_1Answer = prompt(`${player_1}, угадай число от 0 до 10`)
            if(player_1Answer.toLowerCase() == exit){
                alert(`${player_1} ушёл из игры.`)
                player_1 = false;
            }else if(player_1Answer == answer){
                alert(`${player_1} угадал число!`)
                continue;
            }else{
                alert(`${player_1}, неверно.`)
            }
        }
        if(player_2){
            player_2Answer = prompt(`${player_2}, угадай число от 0 до 10`)
            if(player_2Answer.toLowerCase() == exit){
                alert(`${player_2} ушёл из игры.`)
                player_2 = false;
            }else if(player_2Answer == answer){
                alert(`${player_2} угадал число!`)
                continue;
            }else{
                alert(`${player_2}, неверно.`)
            }
        }
    }
} else {
    alert('Некому играть!\nДля игры нужно ввести хотябы одно имя.')
}