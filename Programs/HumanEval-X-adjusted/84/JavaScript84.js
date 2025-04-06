
const solve = (N) => {
  let t = 0
  while (N > 0) {
    t += N % 10
    N = (N - N % 10) / 10
  }
  return t.toString(2)
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = solve(...args);
console.log(result);