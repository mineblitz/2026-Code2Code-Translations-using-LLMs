
const isPrime = (n) => {
  if (n < 2)
    return false;
  for (let k = 2; k < n - 1; k++)
    if (n % k == 0)
      return false;
  return true;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = isPrime(...args);
console.log(result);