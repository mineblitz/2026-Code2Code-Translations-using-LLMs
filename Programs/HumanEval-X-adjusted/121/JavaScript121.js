
const solution = (lst) => {
  let p = 0
  for (let i = 0; i < lst.length; i += 2) {
    if (lst[i] % 2 == 1) {
      p += lst[i]
    }
  }
  return p
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = solution(...args);
console.log(result);