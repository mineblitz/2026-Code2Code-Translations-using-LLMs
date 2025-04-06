
const isSimplePower = (x, n) => {
  if (n == 1)
    return (x == 1);
  var power = 1;
  while (power < x)
    power = power * n;
  return (power == x);
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = isSimplePower(...args);
console.log(result);