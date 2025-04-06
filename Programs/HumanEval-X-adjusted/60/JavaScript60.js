
const sumToN = (n) => {
  return n * (n + 1) / 2;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = sumToN(...args);
console.log(result);