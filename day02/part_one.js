
const fs = require('fs');

const content = fs.readFileSync('./input', 'utf8');

contentArray = content.split('\n');

contentArray.pop();

let countValidPassword = 0;

const inRange = (min, max, count) => {
    return (count >= min) && (count <= max);
}

contentArray.forEach(content => {
    const min = parseInt(content.substr(0, content.indexOf('-')));
    const max = parseInt(content.slice(1 + content.indexOf('-')));
    const letter = content[content.indexOf(':') - 1];
    const password = content.slice(2 + content.indexOf(':'));
    let letterCount = 0;
    for (const char of password) {
        if (char === letter) {
            ++letterCount;
        }
    }
    if (inRange(min, max, letterCount)) {
        ++countValidPassword;
        //console.log(min + '-' + max + ' ' + letter + '\t' + letterCount);
    }
});

console.log(countValidPassword);
