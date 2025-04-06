
const eat = (number, need, remaining) => {
  if (need <= remaining) {
    return [need + number, remaining - need]
  }
  return [remaining + number, 0]
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
args[1] = parseInt(args[1]);
args[2] = parseInt(args[2]);
// Call the function and print the result
const result = eat(...args);
console.log(result);