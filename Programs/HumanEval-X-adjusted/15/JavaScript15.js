
const stringSequence = (n) => {
  return [...Array(n).keys(), n].join(' ')
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = stringSequence(...args);
console.log(result);