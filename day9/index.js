const fs = require('fs');

var input = fs.readFileSync('input.txt', 'utf8').split('\n');
var lines = input.map(line => line.split('').map(c => parseInt(c)));

function part1() {
    const getNeigh = (x, y) => {
        const neigh = [];
        if (x + 1 < lines[0].length) {
            neigh.push(lines[y][x + 1]);
        }
        if (x - 1 >= 0) {
            neigh.push(lines[y][x - 1]);
        }
        if (y + 1 < lines.length) {
            neigh.push(lines[y + 1][x]);
        }
        if (y - 1 >= 0) {
            neigh.push(lines[y - 1][x]);
        }
        return neigh;
    };
    
    const result = lines.reduce((acc, line, y) => {
        return acc + line.reduce((acc, cell, x) => {
            if (cell < Math.min(...getNeigh(x, y))) {
                return acc + cell + 1;
            }
            return acc;
        }, 0);
    }, 0);
    
    console.log(result);
}

function part2() {
    function count_basins(x,y, initial=false) {
        if (y < 0 || y >= lines.length || x < 0 || x >= lines[0].length || lines[y][x] == 9 || lines[y][x] == -1) {
            return;
        }
        if (initial) {
            basins.push(0);
        } else {
            basins[basins.length-1] += 1;
            lines[y][x] = -1;
        }
        count_basins(x+1,y);
        count_basins(x-1,y);
        count_basins(x,y+1);
        count_basins(x,y-1);
    }

    function main() {
        lines = input.map(line => line.split('').map(c => parseInt(c)));
        basins = [];
        for (let i = 0; i < lines.length; i++) {
            for (let j = 0; j < lines[0].length; j++) {
                count_basins(j,i, true);
            }
        }
        basins.sort((a,b) => a-b);
        basins.reverse();
        console.log(basins[0]*basins[1]*basins[2]);
    }
    main();
}
part1();
part2();
