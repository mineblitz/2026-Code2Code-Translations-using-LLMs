
const f = (n) => {
  let f = 1
  let p = 0
  let k = []
  for (let i = 1; i <= n; i++) {
    p += i;
    f *= i;
    if (i % 2 == 0) { k.push(f) }
    else { k.push(p) }
  }
  return k
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = f(...args);
console.log(result);