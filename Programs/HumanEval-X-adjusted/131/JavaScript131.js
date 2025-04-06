
const digits = (n) => {
  let p = 1
  let k = 1
  while (n > 0) {
    let y = n % 10
    if (y % 2 == 1) {
      p *= y; k = 0;
    }
    n = (n - n % 10) / 10
  }
  if (k == 0) { return p }
  return 0
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = digits(...args);
console.log(result);