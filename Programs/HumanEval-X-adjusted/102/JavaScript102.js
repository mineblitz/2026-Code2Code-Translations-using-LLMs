
const chooseNum = (x, y) => {
  for (let i = y; i >= x; i--) {
    if (i % 2 == 0) {return i }
  }
  return -1
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
// Call the function and print the result
const result = chooseNum(...args);
console.log(result);