const fs = require("fs")

try {
    var data = fs.readFileSync('input.txt', 'utf8');   
} catch(e) {
    console.log('Error:', e.stack);
}

function parse(t) {
    return t.trim().split('\n').map(function(line) {
        return line.split('').map(function(b) {
            return parseInt(b);
        });
    });
}
function toDec(a) {
    return a.reduce(function(p, c, i) {
        return p + c * Math.pow(2, a.length - i - 1);
    }, 0);
}
function countOnes(matrix, col) {
    return matrix.reduce(function(p, c) {
        return p + c[col];
    }, 0);
}
function part1(text) {
    var parsed = parse(text);
    var n = parsed.length;
    var gamma = 0;
    var colSize = parsed[0].length;
    for (var col = 0; col < colSize; col++) {
        var ones = countOnes(parsed, col);
        var zeros = n - ones;
        if (ones > zeros) {
            var p = colSize - 1 - col;
            gamma += Math.pow(2, p);
        }
    }
    var allOnes = Math.pow(2, colSize) - 1;
    var epsilon = ~gamma & allOnes;
    return gamma * epsilon;
}
function calculateRating(matrix, rules) {
    for (var col = 0; col < matrix[0].length; col++) {
        var n = matrix.length;
        if (n === 1) {
            break;
        }
        var ones = countOnes(matrix, col);
        var zeros = n - ones;
        if (ones >= zeros) {
            var keepBit = rules[1];
        } else {
            var keepBit = rules[0];
        }
        matrix = matrix.filter(function(element) {
            return element[col] === keepBit;
        });
    }
    return toDec(matrix[0]);
}
function part2(text) {
    var parsed = parse(text);
    var oxygen = calculateRating(parsed, [0, 1]);
    var co = calculateRating(parsed, [1, 0]);
    return oxygen * co;
}

console.log(part1(data), part2(data))
