
const fib4 = (n) => {
  var results = [0, 0, 2, 0];
  if (n < 4)
    return results[n];
  for (let i = 4; i < n + 1; i++) {
    results.push(results.at(-1) + results.at(-2) +
                results.at(-3) + results.at(-4));
    results.shift();
  }
  return results.pop();
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = fib4(...args);
console.log(result);