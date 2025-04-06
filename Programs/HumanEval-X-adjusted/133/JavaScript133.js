
const sumSquares = (lst) => {
  let p = 0
  for (let i = 0; i < lst.length; i++) {
    let y = lst[i]
    if (y % 1 != 0) {
      if (y > 0) { y = y - y % 1 + 1 }
      else { y = -y; y = y - y % 1 }
    }
    p += y * y
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = sumSquares(...args);
console.log(result);