
const primeFib = (n) => {
  var isPrime = function (p) {
    if (p < 2)
      return false;
    for (let k = 2; k < Math.min(Math.floor(Math.sqrt(p)) + 1, p - 1); k++) {
      if (p % k == 0)
        return false;
    }
    return true;
  }

  var f = [0, 1];
  while (true) {
    f.push(f.at(-1) + f.at(-2));
    if (isPrime(f.at(-1)))
      n -= 1;
    if (n == 0)
      return f.at(-1);
  }
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = primeFib(...args);
console.log(result);