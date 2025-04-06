
const getMaxTriples = (n) => {
  let y = []
  for (let i = 1; i <= n; i++) {
    y.push(i * i - i + 1)
  }
  let u = 0
  for (let i = 0; i < n - 2; i++) {
    for (let j = i + 1; j < n - 1; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((y[i] + y[j] + y[k]) % 3 == 0) { u++ }
      }
    }
  }
  return u
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = getMaxTriples(...args);
console.log(result);