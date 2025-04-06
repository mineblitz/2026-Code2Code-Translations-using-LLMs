
const fib = (n) => {
  if (n == 0)
    return 0;
  if (n == 1)
    return 1;
  return fib(n - 1) + fib(n - 2);
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = fib(...args);
console.log(result);