
const countUpTo = (n) => {
  let t = []
  for (let i = 2; i < n; i++) {
    let p = 1
    for (let j = 2; j * j <= i; j++) {
      if (i % j == 0) { p = 0; break }
    }
    if (p == 1) { t.push(i) }
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = countUpTo(...args);
console.log(result);