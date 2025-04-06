
const isMultiplyPrime = (a) => {
  var isPrime = function (n) {
    for (let j = 2; j < n; j++)
      if (n % j == 0)
        return false;
    return true;
  }

  for (let i = 2; i < 101; i++) {
    if (!isPrime(i)) continue;
    for (let j = 2; j < 101; j++) {
      if (!isPrime(j)) continue;
      for (let k = 2; k < 101; k++) {
        if (!isPrime(k)) continue;
        if (i*j*k == a)
          return true;
      }
    }
  }
  return false;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = isMultiplyPrime(...args);
console.log(result);