
const fs = require('fs');

const content = fs.readFileSync('./input', 'utf8');

contentArray = content.split('\n');

contentArray.pop();

let countValidPassword = 0;

const isValid = (i, j, str, c) => {
    return (str[i] === c) || (str[j] === c);
}

contentArray.forEach(content => {
    const first = parseInt(content.substr(0, content.indexOf('-')));
    const second = parseInt(content.slice(1 + content.indexOf('-')));
    const letter = content[content.indexOf(':') - 1];
    const password = content.slice(2 + content.indexOf(':'));

    if (isValid(first, second, password, letter)) {
        ++countValidPassword;
    }
});

console.log(countValidPassword);
