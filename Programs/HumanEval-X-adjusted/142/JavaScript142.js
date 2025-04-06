
const sumSquares = (lst) => {
  let y = 0
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 == 0) { y += lst[i] * lst[i] }
    else if (i % 4 == 0) { y += lst[i] * lst[i] * lst[i] }
    else { y += lst[i] }
  }
  return y
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = sumSquares(...args);
console.log(result);