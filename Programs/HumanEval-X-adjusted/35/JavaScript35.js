
const maxElement = (l) => {
  return Math.max(...l);
}

// Get the command-line arguments
const args = process.argv.slice(2);
args[0] = args[0].replace(/'/g, '"');
args[0] = JSON.parse(args[0]);
// Call the function and print the result
const result = maxElement(...args);
console.log(result);