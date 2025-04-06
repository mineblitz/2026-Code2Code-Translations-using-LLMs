
const specialFactorial = (n) => {
  let p = 1;
  let t = 1;
  while (n > 1) {
    let y = p;
    while (y > 0) {
      y--;
      t *= n;
    }
    p++;
    n--;
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = specialFactorial(...args);
console.log(result);