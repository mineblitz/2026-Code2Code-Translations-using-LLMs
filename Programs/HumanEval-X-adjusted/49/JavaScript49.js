
const modp = (n, p) => {
  var ret = 1;
  for (let i = 0; i < n; i++)
    ret = (2 * ret) % p;
  return ret;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = modp(...args);
console.log(result);