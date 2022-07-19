let tryCount = 3;
for(let i = 1; i <= tryCount; i++){
    var answer = prompt('Зимой и летом одним цветом:').toLowerCase();
    if(answer == 'ёлка' || answer == 'ель' || answer == 'елка'){
        alert(`Правильно! Это ${answer}, игра окончена.`)
        break;
    } else{
        if(i == tryCount){
            alert(`Неверно!\nЭто же Ёлка!`)
        }
            alert(`Неверно!\nПопыток осталось ${tryCount - i}`)
    }
}

let correctAnswersCount = 0;
let correctAnswer;
let riddleContent = [['Сколько будет 3+3*3?', ['12', 'двенадцать']], ['Два конца, два кольца, посредине гвоздик.', ['ножницы']],['Не огонь, а жжется.', ['крапива']]];

alert('А теперь 3 загадки с одной попыткой!\nЗа каждый правильный ответ +1 балл.')
function GetAndCheckAnswer(i){
    answer = prompt(riddleContent[i][0]).toLowerCase();
    correctAnswer = riddleContent[i][1];
    if(correctAnswer.includes(answer)){
        correctAnswersCount++;
        alert('Молодец, отгадал!\n+1 балл!')
    } else {
        alert(`Нет, не верно!\nЭто ${correctAnswer[0]}`)
    }
}
for(let i = 0; i < tryCount; i++){
    GetAndCheckAnswer(i);
}
document.write(`Количество набранных баллов: ${correctAnswersCount}`)