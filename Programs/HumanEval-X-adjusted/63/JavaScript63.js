
const fibfib = (n) => {
  if (n == 0 || n == 1)
    return 0;
  if (n == 2)
    return 1;
  return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3);
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = fibfib(...args);
console.log(result);