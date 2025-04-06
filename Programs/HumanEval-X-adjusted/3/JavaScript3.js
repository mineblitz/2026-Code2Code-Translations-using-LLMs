
const belowZero = (operations) => {
  var balance = 0;
  for (const op of operations) {
    balance += op;
    if (balance < 0) {
      return true;
    }
  }
  return false;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = belowZero(...args);
console.log(result);