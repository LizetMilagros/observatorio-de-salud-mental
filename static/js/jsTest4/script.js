//seleccionado todos los elementos requeridos
const start_btn = document.querySelector(".start_btn button");
const info_box = document.querySelector(".info_box");
const exit_btn = info_box.querySelector(".buttons .quit");
const continue_btn = info_box.querySelector(".buttons .restart");
const quiz_box = document.querySelector(".quiz_box");
const result_box = document.querySelector(".result_box");
const option_list = document.querySelector(".option_list");


// si el boton de iniciar es presionado
start_btn.onclick = () => {
    info_box.classList.add("activeInfo"); //mostrar la informacion en la caja
}

// si el boton de salir es presionado
exit_btn.onclick = () => {
    info_box.classList.remove("activeInfo"); //hide info box
}

// si el boton de continuar es presionado
continue_btn.onclick = () => {
    info_box.classList.remove("activeInfo"); //hide info box
    quiz_box.classList.add("activeQuiz"); //show quiz box
    showQuetions(0); //calling showQestions function
    queCounter(1); //passing 1 parameter to queCounter
}

let que_count = 0;
let que_numb = 1;
let userScore = 0;
let counter;
let counterLine;
let widthValue = 0;

const restart_quiz = result_box.querySelector(".buttons .restart");
const quit_quiz = result_box.querySelector(".buttons .quit");

// si el boton de reiniciar es presionado
restart_quiz.onclick = () => {
    quiz_box.classList.add("activeQuiz"); //show quiz box
    result_box.classList.remove("activeResult"); //hide result box
    que_count = 0;
    que_numb = 1;
    userScore = 0;
    widthValue = 0;
    showQuetions(que_count); //calling showQestions function
    queCounter(que_numb); //passing que_numb value to queCounter
    clearInterval(counter); //clear counter
    clearInterval(counterLine); //clear counterLine
    next_btn.classList.remove("show"); //hide the next button
}

// si el boton de salir del test es presionado
quit_quiz.onclick = () => {
    window.location.reload(); //reload the current window
}

const next_btn = document.querySelector("footer .next_btn");
const bottom_ques_counter = document.querySelector("footer .total_que");

// si el boton siguiente es presionado
next_btn.onclick = () => {
    if (que_count < questions.length - 1) { //if question count is less than total question length
        que_count++; //increment the que_count value
        que_numb++; //increment the que_numb value
        showQuetions(que_count); //calling showQestions function
        queCounter(que_numb); //passing que_numb value to queCounter
        clearInterval(counter); //clear counter
        clearInterval(counterLine); //clear counterLine
        next_btn.classList.remove("show"); //hide the next button
    } else {
        clearInterval(counter); //clear counter
        clearInterval(counterLine); //clear counterLine
        showResult(); //calling showResult function
    }
}

// getting questions and options from array
function showQuetions(index) {
    const que_text = document.querySelector(".que_text");

    //creating a new span and div tag for question and option and passing the value using array index
    let que_tag = '<span>' + questions[index].numb + ". " + questions[index].question + '</span>';
    let option_tag = '<div class="option"><span>' + questions[index].options[0] + '</span></div>' +
        '<div class="option"><span>' + questions[index].options[1] + '</span></div>' +
        '<div class="option"><span>' + questions[index].options[2] + '</span></div>' +
        '<div class="option"><span>' + questions[index].options[3] + '</span></div>' +
        '<div class="option"><span>' + questions[index].options[4] + '</span></div>';
    que_text.innerHTML = que_tag; //adding new span tag inside que_tag
    option_list.innerHTML = option_tag; //adding new div tag inside option_tag

    const option = option_list.querySelectorAll(".option");

    // set onclick attribute to all available options
    for (i = 0; i < option.length; i++) {
        option[i].setAttribute("onclick", "optionSelected(this)");
    }
}
// creando las nuevas  etiquetas div para los iconos
let tickIconTag = '<div class="icon tick"><i class="fas fa-check"></i></div>';
let crossIconTag = '<div class="icon cross"><i class="fas fa-times"></i></div>';

//si el usuario clikea una opción
function optionSelected(answer) {
    clearInterval(counter); //clear counter
    clearInterval(counterLine); //clear counterLine
    let userAns = answer.textContent; //getting user selected option
    const allOptions = option_list.children.length; //getting all option items

    switch (userAns) {
        case "a) Completamente en desacuerdo":
            userScore += 0;
            break;
        case "b) En desacuerdo":
            userScore += 1;
            break;
        case "c) Indeciso":
            userScore += 2;
            break;
        case "d) Deacuerdo":
            userScore += 3;
            break;
        case "e) Completamente de acuerdo":
            userScore += 4;
            break;
    }
    next_btn.classList.add("show"); //show the next button if user selected any option
}

function showResult() {
    info_box.classList.remove("activeInfo"); //hide info box
    quiz_box.classList.remove("activeQuiz"); //hide quiz box
    result_box.classList.add("activeResult"); //show result box
    const scoreText = result_box.querySelector(".score_text");
    const infoText = result_box.querySelector(".info_text");
    let scoreTag = '<span>Usted tiene una puntuación de<p>' + userScore + '</p></span>';
    let info = '<span> Podemos interpretar la puntuacion de la siguiente manera. Cuando tenemos una puntuación entre 0 y 12 tenemos los síntomas de una psicosis leve o inexistente. Cuando obtenemos una puntuación entre 12 y 24 corresponde a una psicosis moderada, cuando obtenemos una puntuación entre 24 y 36 corresponde a una psicosis moderadamente alta, ya puede causar preocupación en nosotros, y finalmente si obtenemos una puntuación mayor a 36 es un nivel alto y debemos acudir ante un especialista y obtener más información al respecto. </span>';
    scoreText.innerHTML = scoreTag; //adding new span tag inside score_Text
    infoText.innerHTML = info;
}

function queCounter(index) {
    //creating a new span tag and passing the question number and total question
    let totalQueCounTag = '<span><p>' + index + '</p> de <p>' + questions.length + '</p> Sintomas</span>';
    bottom_ques_counter.innerHTML = totalQueCounTag; //adding new span tag inside bottom_ques_counter
}