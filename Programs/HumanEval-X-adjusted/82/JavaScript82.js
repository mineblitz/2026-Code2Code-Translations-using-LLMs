
const primeLength = (string) => {
  let len = string.length
  if (len == 1 || len == 0) { return false }
  for (let i = 2; i * i <= len; i++) {
    if (len % i == 0) { return false }
  }
  return true
}

// Get the command-line arguments
const args = process.argv.slice(2);
// Call the function and print the result
const result = primeLength(...args);
console.log(result);