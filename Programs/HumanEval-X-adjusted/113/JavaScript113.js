
const oddCount = (lst) => {
  let d = []
  for (let i = 0; i < lst.length; i++) {
    let p = 0;
    let h = lst[i].length
    for (let j = 0; j < h; j++) {
      if (lst[i][j].charCodeAt() % 2 == 1) { p++ }
    }
    p = p.toString()
    d.push('the number of odd elements ' + p + 'n the str' + p + 'ng ' + p + ' of the ' + p + 'nput.')
  }
  return d
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = oddCount(...args);
console.log(result);