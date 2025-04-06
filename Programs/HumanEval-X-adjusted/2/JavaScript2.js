
const truncateNumber = (number) => {
  return number % 1.0;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseFloat(args[0]);
// Call the function and print the result
const result = truncateNumber(...args);
console.log(result);