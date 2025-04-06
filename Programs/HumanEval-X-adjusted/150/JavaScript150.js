
const xOrY = (n, x, y) => {
  let len = n
  if (len == 1 || len == 0) { return y }
  for (let i = 2; i * i <= len; i++) {
    if (len % i == 0) { return y }
  }
  return x
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
args[2] = parseInt(args[2]);
// Call the function and print the result
const result = xOrY(...args);
console.log(result);