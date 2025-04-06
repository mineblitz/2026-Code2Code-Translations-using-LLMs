
const largestPrimeFactor = (n) => {
  var isPrime = function (k) {
    if (k < 2)
      return false;
    for (let i = 2; i < k - 1; i++)
      if (k % i == 0)
        return false;
    return true;
  }

  var largest = 1;
  for (let j = 2; j < n + 1; j++)
    if (n % j == 0 && isPrime(j))
      largest = Math.max(largest, j);
  return largest;
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = largestPrimeFactor(...args);
console.log(result);