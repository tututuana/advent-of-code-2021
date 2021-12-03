const fs = require("fs");
const levels = fs.readFileSync("input.txt", "utf8").split("\n").map(Number);

const count = (step) => {
    let sum = 0;
    for (let i = 0; i < levels.length - step; i++) {
        if (levels[i] < levels[i + step]) {
            sum++;
        }
    }
    return sum;
}

console.log(count(1), count(3));
