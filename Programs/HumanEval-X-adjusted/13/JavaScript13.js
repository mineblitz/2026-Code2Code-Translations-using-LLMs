
const greatestCommonDivisor = (a, b) => {
  while (b != 0) {
    let temp = a;
    a = b;
    b = temp % b;
  }
  return a;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = greatestCommonDivisor(...args);
console.log(result);