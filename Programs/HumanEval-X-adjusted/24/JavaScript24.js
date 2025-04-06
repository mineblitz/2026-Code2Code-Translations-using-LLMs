
const largestDivisor = (n) => {
  for (let i = n - 1; i >= 0; i--)
    if (n % i == 0)
      return i;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = largestDivisor(...args);
console.log(result);