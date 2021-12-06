const fs = require('fs');
var input = fs.readFileSync('input.txt').toString().split(",").map(Number);
var fishs = {};
for (var age = 0; age < 9; age++) {
    fishs[age] = input.filter(function(x){return x == age}).length;
}
function ticks(f) {
    var newborn = f[0];
    for (var i = 0; i < 8; i++) {
        if (i != 6) f[i] = f[i+1];
        else f[i] = f[i+1]+newborn;
    }
    f[8] = newborn;
    return f;
}
for (var i = 0; i < 256; i++) {
    fishs = ticks(fishs);
    if (i == 79) console.log("1: ", Object.values(fishs).reduce(function(a,b){return a+b}));
}
console.log("2: ", Object.values(fishs).reduce(function(a,b){return a+b}));
