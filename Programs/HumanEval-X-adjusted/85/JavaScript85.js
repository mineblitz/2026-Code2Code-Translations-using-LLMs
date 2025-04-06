
const add = (lst) => {
  let t = 0
  for (let i = 1; i < lst.length; i += 2) {
    if (lst[i] % 2 == 0) {
      t += lst[i]
    }
  }
  return t
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = add(...args);
console.log(result);