
const tri = (n) => {
  if (n == 0) { return [1] }
  if (n == 1) { return [1, 3] }
  let p = [1, 3]
  for (let i = 2; i <= n; i++) {
    if (i % 2 == 0) {
      p.push(1 + i / 2)
    }
    else {
      p.push(p[i - 2] + p[i - 1] + 1 + (i + 1) / 2)
    }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = tri(...args);
console.log(result);