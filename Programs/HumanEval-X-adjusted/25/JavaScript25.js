
const factorize = (n) => {
  var fact = [], i = 2;
  while (i <= Math.sqrt(n) + 1) {
    if (n % i == 0) {
      fact.push(i);
      n = n / i;
    } else {
      i += 1;
    }
  }

  if (n > 1)
    fact.push(n);
  return fact;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = factorize(...args);
console.log(result);