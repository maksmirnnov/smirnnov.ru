//объявляю переменные через let потому что var устарел.
//Курс валют, который я задаю сам (мог бы сделать сложнее и получать эти данные с сервера, но не стал для простоты примера)
let usdRate = 75.29;
let eurRate = 90.50;
//Результат конвертирования рублей в валюту (пока что пишем 0)
let usdConverted = 0;
let eurConverted = 0;
//получаю элементы страницы и вношу их в соответствующие переменные
let input = document.getElementById('input')                    //поле ввода
let btn = document.getElementById('convert-btn')                //кнопка
let usdRateValue = document.getElementById('usd-rate-value')    //курс USD
let eurRateValue = document.getElementById('eur-rate-value')    //курс EUR
let usdResValue = document.getElementById('usd-res-value')      //результат конвертирования RUB в USD
let eurResValue = document.getElementById('eur-res-value')      //результат конвертирования RUB в EUR
//Теперь создаю функцию, которая будет переводить наши рубли в валюту
function convert(){
  usdConverted = (input.value/usdRate).toFixed(2) //перевод в USD. Метод toFixed(2) округляет значение до 2 знаков после запятой
  eurConverted = (input.value/eurRate).toFixed(2) //перевод в EUR
  usdRateValue.innerText = usdRate.toFixed(2); //innerText - метод, позволяющий получить или изменить текст в элементе страницы
  eurRateValue.innerText = eurRate.toFixed(2);
  usdResValue.innerText = usdConverted;
  eurResValue.innerText = eurConverted;
}
//Теперь вешаем на кнопку прослушку события, где первым аргументом мы передаём тип события (клик), а вторым
// аргументом передаём нашу функцию.
btn.addEventListener('click', convert)
//Теперь браузер будет слушать событие клика на нашу кнопку и при клике на неё будет вызывать нашу функцию convert.
//Можете посетить мой сайт - https://smirnnov-dev.web.app/