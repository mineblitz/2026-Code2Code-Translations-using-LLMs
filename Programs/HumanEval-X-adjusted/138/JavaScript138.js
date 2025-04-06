
const isEqualToSumEven = (n) => {
  return (n >= 8 && n % 2 == 0)
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = isEqualToSumEven(...args);
console.log(result);