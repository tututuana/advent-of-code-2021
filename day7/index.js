function part1(inp) {
    inp = inp.split(",").map(Number);
    var minx = Math.min.apply(null, inp);
    var maxx = Math.max.apply(null, inp);

    var best = Infinity;

    for (var i = minx; i <= maxx; i++) {
        var cost = inp.map(function(j) { return Math.abs(i - j); }).reduce(function(a, b) { return a + b; });
        if (cost < best) {
            best = cost;
        }
    }

    console.log(best);
}

function part2(inp) {
  inp = inp.split(",").map(Number);
  minx = Math.min.apply(null, inp);
  maxx = Math.max.apply(null, inp);

  let best = Infinity;

  function f(n) {
      return (n * (n + 1)) / 2;
  }

  for (let i = minx; i <= maxx; i++) {
      let cost = inp.reduce((acc, j) => acc + f(Math.abs(i - j)), 0);
      if (cost < best) {
          best = cost;
      }
  }

  console.log(best);
}

const fs = require("fs")
const input = fs.readFileSync("input.txt", "utf8");
part1(input); part2(input);
