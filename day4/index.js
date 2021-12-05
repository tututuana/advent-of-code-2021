// Paste it to the console.
// https://raw.githubusercontent.com/tututuana/advent-of-code-2021/main/day4/input.txt

input = document.body.textContent.split("\n")

function Board(data) {
  this.numbers = data.map(line => line.trim().split(/\s+/).map(s => parseInt(s, 10)))
  this.marked = Array.from(Array(5), () => Array(5).fill(false))
}

Board.prototype.indexOf = function(number) {
  for (const [i, row] of this.numbers.entries()) {
    for (const [j, _number] of row.entries()) {
      if (number === _number) {
        return [i, j];
      }
    }
  }
  return [null, null];
}

Board.prototype.mark = function(number) {
  const [i, j] = this.indexOf(number);
  if (i !== null && j !== null) {
    this.marked[i][j] = true;
  }
}

Object.defineProperty(Board.prototype, "winner", {
  get() {
    for (let i = 0; i < 5; i++) {
      let row = true,
        col = true;
      for (let j = 0; j < 5; j++) {
        row &&= this.marked[i][j];
        col &&= this.marked[j][i];
      }
      if (row || col) {
        return true
      }
    }
    return false;
  }
})

Object.defineProperty(Board.prototype, "unmarked", {
  get() {
    let sum = 0;
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        sum += this.numbers[i][j] * !this.marked[i][j];
      }
    }
    return sum;
  }
})

draw = input[0].trim().split(",").map(s => parseInt(s, 10))
boards = []
for (let i = 2; i < input.length; i += 6) { boards.push(new Board(input.slice(i, i + 5))) }

function markAll(number) { boards.forEach(board => board.mark(number)); }

won = false;
for (const number of draw) {
  markAll(number);
  boards = boards.filter(b => {
    if (b.winner) {
      if (!won) {
        won = true;
        console.log(`1: ${b.unmarked * number}`);
      }
      if (boards.length === 1) {
        console.log(`2: ${b.unmarked * number}`);
      }
      return false;
    }
    return true;
  })
}
