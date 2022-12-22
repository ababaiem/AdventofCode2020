
const fs = require('fs');

const content = fs.readFileSync('./input', 'utf8');

contentArray = content.split('\n');

contentArray.pop();

listNumbers = contentArray.map((n) => {
    return parseInt(n, 10);
});

const is2020 = (x, y) => {
    return (x + y) === 2020;
}

const answer = () => {
    for (const firstNumber of listNumbers) {
        for (const secondNumber of listNumbers) {
            if (is2020(firstNumber, secondNumber)) {
                return (firstNumber * secondNumber);
            }
        }
    }
}

console.log(answer().toString());
