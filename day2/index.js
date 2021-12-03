const fs = require("fs")

function read_data() {
    var output = [];
    var data = fs.readFileSync("text.txt", "utf8");
    data.split("\n").forEach(function(line) {
        output.push(line.split(" "));
    });
    return output;
}

var data = read_data();

function part1() {
    var depth = 0;
    var horizontal = 0;
    data.forEach(function(line) {
        if (line[0] == "down") {
            depth += parseInt(line[1]);
        } else if (line[0] == "up") {
            depth -= parseInt(line[1]);
        } else if (line[0] == "forward") {
            horizontal += parseInt(line[1]);
        }
    });
    return depth * horizontal;
}

function part2() {
    var aim = 0;
    var horiz = 0;
    var depth = 0;
    data.forEach(function(line) {
        if (line[0] == "down") {
            aim += parseInt(line[1]);
        } else if (line[0] == "up") {
            aim -= parseInt(line[1]);
        } else if (line[0] == "forward") {
            horiz += parseInt(line[1]);
            depth += aim * parseInt(line[1]);
        }
    });
    return depth * horiz;
}

console.log(part1(), part2());
