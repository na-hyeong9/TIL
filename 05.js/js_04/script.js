const button = document.querySelector('#lotto-btn')
button.addEventListener('click', function () {
    // 컨테이너를 만들고
    const ballContainer = document.createElement('div')
    ballContainer.classList.add('ball-container')

    // 공을 만들어서 =>  6개를 만들어서
    const numbers = _.sampleSize(_.range(1, 46), 6)
    console.log(numbers)
    numbers.sort((a, b) => a - b);
    for (number of numbers) {
        const ball = document.createElement('div')
        ball.classList.add('ball')
        ball.innerText = number
        if (1 <= number & number <= 10) {
            ball.style.borderColor = "orange";
        }
        else if (number <= 20) {
            ball.style.borderColor = "red";
        }
        else if (number <= 30) {
            ball.style.borderColor = "blue";

        }
        else if (number <= 40) {
            ball.style.borderColor = "green";

        }
        else if (number <= 45) {
            ball.style.borderColor = "puple";

        }

        // 컨테이너에 붙인다.
        // ballContainer.appendChild(ball)
        ballContainer.appendChild(ball)
    }

    // 컨테이너를 결과 영역에 붙인다. 
    const result = document.querySelector('#result')
    result.prepend(ballContainer)

})