
const decimalToBinary = (decimal) => {
  return "db" + decimal.toString(2) + "db";
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = decimalToBinary(...args);
console.log(result);