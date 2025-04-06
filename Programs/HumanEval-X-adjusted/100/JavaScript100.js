
const makeAPile = (n) => {
  let t = []
  for (let i = n; i < n * 3; i += 2) {
    t.push(i)
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
// Call the function and print the result
const result = makeAPile(...args);
console.log(result);