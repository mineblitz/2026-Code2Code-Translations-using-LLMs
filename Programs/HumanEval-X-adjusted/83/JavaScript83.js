
const startsOneEnds = (n) => {
  if (n == 1) { return 1 }
  let t = 18
  for (let i = 2; i < n; i++) {
    t = t * 10
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = startsOneEnds(...args);
console.log(result);